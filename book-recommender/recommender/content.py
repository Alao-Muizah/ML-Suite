import numpy as np 
from recommender.utils import load_books_with_genre

# ================ GETTING RECOMMENDATIONS BY GENRE =========================== #

def recommend_by_genre(selected_genres, top_n = 10):

    books = load_books_with_genre()

    mask = books['Genres'].apply(
        lambda x: any(g in x for g in selected_genres)
    )

    matched = books[mask].copy()

    if matched.empty:
        return matched 
    
    matched['score'] = (
    0.7 * matched['Avg_rating'] +
    0.3 * np.log1p(matched['Num_rating'])
)

    return matched.sort_values('score', ascending=False).head(top_n)[
        ['ISBN', 'Book-Title', 'Book-Author', 'Avg_rating', 'Num_rating', 'Genres', 'Cover']
    ].reset_index(drop=True)



