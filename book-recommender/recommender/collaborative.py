import joblib 
from recommender.utils import load_data, load_books_with_genre
from pathlib import Path 

BASE_DIR = Path(__file__).parent.parent
MODELS_DIR = BASE_DIR / "models"


# ================ GETTING RECOMMENDATIONS BY BOOKS =========================== #

def recommend_by_books(user_read_titles, top_n=10):

    filtered_books, ratings_filtered = load_data()
    books_with_genre = load_books_with_genre()

    selected_isbns = filtered_books[filtered_books['Book-Title'].isin(user_read_titles)]['ISBN'].values 

    liked = ratings_filtered[
        (ratings_filtered['ISBN'].isin(selected_isbns)) & 
        (ratings_filtered['Book-Rating'] >= 8)
    ]

    if liked.empty:
        return books_with_genre.iloc[0:0]
    
    similar_users = liked['User-ID'].unique()
    candidate_ratings = ratings_filtered[ratings_filtered['User-ID'].isin(similar_users)]
    
    candidate_isbns = [
        isbn for isbn in candidate_ratings['ISBN'].unique()
        if isbn not in selected_isbns
    ]

    if not candidate_isbns:
        return books_with_genre.iloc[0:0]
    
    model = joblib.load(MODELS_DIR / "svd_model.pkl")
    predictions = []
    for isbn in candidate_isbns:
        pred = model.predict(uid=0, iid=isbn)
        predictions.append((isbn, pred.est))

    predictions.sort(key=lambda x: x[1], reverse=True)    
    top_isbns = [isbn for isbn, _ in predictions[:top_n]]

    result = books_with_genre[books_with_genre['ISBN'].isin(top_isbns)][
        ['ISBN', 'Book-Title', 'Book-Author', 'Avg_rating', 'Num_rating', 'Genres', 'Cover']
    ].reset_index(drop=True) 

    return result 

