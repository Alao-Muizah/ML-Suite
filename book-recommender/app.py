import streamlit as st
import pandas as pd
from recommender.content import recommend_by_genre
from recommender.collaborative import recommend_by_books
from recommender.utils import load_books_with_genre

st.set_page_config(page_title="BookMatch", layout="wide")
st.title(" BookMatch")
st.markdown("_Find your next favourite book._")

# ========== Load books for the returning user book selector ========= #
@st.cache_data
def get_book_titles():
    books = load_books_with_genre()
    return sorted(books['Book-Title'].tolist())

GENRES = [
    "Fantasy", "Romance", "Horror", "Adventure", "Mystery",
    "Sci-Fi", "Thriller", "Historical", "Biography", "Non-Fiction", "Young Adult"
]

st.divider()

# =========== USER TYPE ================================================ #
user_type = st.radio(
    "Are you a new reader or returning reader?",
    ["I'm new to reading", "I've read some books"],
    horizontal=True
)

st.divider()

# ============= NEW READER ======================================= #
if user_type == "I'm new to reading":
    st.subheader("Pick genres you enjoy")
    selected_genres = st.multiselect(
        "Select one or more genres",
        options=GENRES
    )

    if st.button("Get Recommendations"):
        if not selected_genres:
            st.warning("Please select at least one genre.")
        else:
            with st.spinner("Finding books for you..."):
                results = recommend_by_genre(selected_genres)

            if results.empty:
                st.info("No books found for those genres. Try different ones.")
            else:
                # NEW READER results
                st.subheader("Recommended for you")
                cols = st.columns(5)
                for i, (_, row) in enumerate(results.iterrows()):
                    with cols[i % 5]:
                        st.markdown(
                            f'<a href="https://openlibrary.org/isbn/{row["ISBN"]}" target="_blank">'
                            f'<img src="{row["Cover"]}" width="100%"></a>',
                            unsafe_allow_html=True
                        )
                        st.markdown(f"**{row['Book-Title']}**")
                        st.markdown(f"*{row['Book-Author']}*")
                        st.markdown(f"⭐ {row['Avg_rating']:.1f} ({int(row['Num_rating'])} ratings)")
                        st.markdown(f"`{'`, `'.join(row['Genres'])}`")

# ====================== RETURNING READER ================================= #
else:
    st.subheader("Select books you have already read and enjoyed")
    book_titles = get_book_titles()
    selected_books = st.multiselect(
        "Search and select books",
        options=book_titles
    )

    if st.button("Get Recommendations"):
        if not selected_books:
            st.warning("Please select at least one book.")
        else:
            with st.spinner("Finding books similar to your taste..."):
                results = recommend_by_books(selected_books)

            if results.empty:
                st.info("Not enough data to recommend based on those books. Try selecting more.")
            else:
                # Usual READER results
                st.subheader("You might also like")
                cols = st.columns(5)
                for i, (_, row) in enumerate(results.iterrows()):
                    with cols[i % 5]:
                        st.markdown(
                            f'<a href="https://openlibrary.org/isbn/{row["ISBN"]}" target="_blank">'
                            f'<img src="{row["Cover"]}" width="100%"></a>',
                            unsafe_allow_html=True
                        )
                        st.markdown(f"**{row['Book-Title']}**")
                        st.markdown(f"*{row['Book-Author']}*")
                        st.markdown(f"{row['Avg_rating']:.1f} ({int(row['Num_rating'])} ratings)")
                        st.markdown(f"`{'`, `'.join(row['Genres'])}`")
st.divider()






