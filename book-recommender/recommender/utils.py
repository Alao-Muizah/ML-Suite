import pandas as pd 
import numpy as np 
import joblib 
from pathlib import Path
import json



BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"


# ================ LOADING DATA =========================== #

def load_data():
    books = pd.read_csv(DATA_DIR / "Books.csv", low_memory=False)
    ratings = pd.read_csv(DATA_DIR / "Ratings.csv")

    books = books[['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher']]
    ratings = ratings[ratings['Book-Rating'] > 0]

    user_counts = ratings['User-ID'].value_counts()
    book_counts = ratings['ISBN'].value_counts()

    ratings_filtered = ratings[
        ratings['User-ID'].isin(user_counts[user_counts >= 10].index) &
        ratings['ISBN'].isin(book_counts[book_counts >= 10].index)
    ]

    filtered_isbns = ratings_filtered['ISBN'].unique()
    filtered_books = books[books['ISBN'].isin(filtered_isbns)].drop_duplicates(subset='ISBN').reset_index(drop=True)

    rating_stats = ratings_filtered.groupby('ISBN').agg(
        Avg_rating = ('Book-Rating', 'mean'),
        Num_rating = ("Book-Rating", 'count')
    ).reset_index()

    filtered_books = filtered_books.merge(rating_stats, on='ISBN', how='left')
    
    return filtered_books, ratings_filtered


# ================ LOADING BOOKS WITH GENRE =========================== # 

def load_books_with_genre():

    path = DATA_DIR / "filtered_books_with_genres.csv"
    books = pd.read_csv(path)
    books['Genres'] = books['Genres'].apply(
        lambda x: json.loads(x.replace("'", '"')) if isinstance(x, str) else []
    )

    books['Cover'] = books['ISBN'].apply(
        lambda x: f"https://covers.openlibrary.org/b/isbn/{x}-M.jpg"
    )
    
    return books 


# ================ LOADING MODEL =========================== #

def load_model():
    return joblib.load(MODELS_DIR / "svd_model.pkl")