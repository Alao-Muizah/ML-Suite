from recommender.utils import load_data, MODELS_DIR
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy
import joblib
import pandas as pd
import json
import time
from groq import Groq
from tqdm import tqdm
from recommender.utils import load_data, DATA_DIR
import os
from pathlib import Path


client = Groq(api_key="API_KEY")


def get_genres_batch(batch_df):
    batch_df = batch_df.reset_index(drop=True)

    books_text = "\n".join([
        f"{i+1}. Title: {row['Book-Title']} | Author: {row['Book-Author']}"
        for i, row in batch_df.iterrows()
    ])

    prompt = f"""
    You are a book classification system.

    Classify each book below. Return ONLY a JSON array, nothing else, no explanation, no markdown backticks.
    Format: [{{"genres": ["genre1", "genre2"]}}]

    One object per book, in the same order as input.
    Use only these genres: Fantasy, Romance, Horror, Adventure, Mystery, Sci-Fi, Thriller, Historical, Biography, Non-Fiction, Young Adult

    Books:
    {books_text}
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content.strip()

        if "```" in result:
            result = result.split("```")[1]
            if result.startswith("json"):
                result = result[4:]

        parsed = json.loads(result.strip())
        return {row['ISBN']: item['genres'] for row, item in zip(batch_df.to_dict('records'), parsed)}

    except Exception as e:
        print(f"Batch failed: {e}")
        return {row['ISBN']: [] for _, row in batch_df.iterrows()}


def classify_genres(filtered_books, checkpoint_name):
    checkpoint_path = DATA_DIR / checkpoint_name

    if checkpoint_path.exists():
        checkpoint = pd.read_csv(checkpoint_path)
        genre_map = dict(zip(checkpoint['ISBN'], checkpoint['Genres']))
        done_isbns = set(genre_map.keys())
        filtered_books = filtered_books[~filtered_books['ISBN'].isin(done_isbns)].reset_index(drop=True)
        print(f"Resuming — {len(done_isbns)} done, {len(filtered_books)} remaining")
    else:
        genre_map = {}

    batch_size = 20

    for i in tqdm(range(0, len(filtered_books), batch_size)):
        batch = filtered_books.iloc[i:i + batch_size]
        result = get_genres_batch(batch)
        genre_map.update(result)

        if i % 100 == 0 and i > 0:
            temp = pd.DataFrame(list(genre_map.items()), columns=['ISBN', 'Genres'])
            temp.to_csv(checkpoint_path, index=False)

        time.sleep(0.3)

    final = pd.DataFrame(list(genre_map.items()), columns=['ISBN', 'Genres'])
    final.to_csv(checkpoint_path, index=False) 
    print(f"Saved {len(final)} books to {checkpoint_path}")
    return final


if __name__ == "__main__":
    print("Loading data...")
    filtered_books, ratings_filtered = load_data()

    print("Classifying genres...")
    genres_data = classify_genres(filtered_books, "genres_checkpoint.csv").drop_duplicates(subset='ISBN')

    final = filtered_books.merge(genres_data, on='ISBN', how='left')
    final['Genres'] = final['Genres'].fillna('[]')
    final.to_csv(DATA_DIR / "filtered_books_with_genres.csv", index=False)
    print(f"Saved filtered_books_with_genres.csv")

    checkpoint_path = DATA_DIR / "genres_checkpoint.csv"
    Path(checkpoint_path).unlink(missing_ok=True)

    print("Training SVD model...")
    reader = Reader(rating_scale=(1, 10))
    data = Dataset.load_from_df(
        ratings_filtered[['User-ID', 'ISBN', 'Book-Rating']], reader
    )
    trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

    model = SVD(n_factors=50, random_state=42)
    model.fit(trainset)

    predictions = model.test(testset)
    print(f"RMSE: {accuracy.rmse(predictions)}")

    joblib.dump(model, MODELS_DIR / "svd_model.pkl")
    print("SVD model saved.")



