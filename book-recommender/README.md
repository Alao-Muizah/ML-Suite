# BookMatch

A hybrid book recommendation system that combines collaborative filtering and content-based filtering to recommend books based on user preferences. Built with Python and deployed as a Streamlit web app.


### Live Demo: [![Streamlit App](https://img.shields.io/badge/Open-Streamlit_App-FF4B4B?logo=streamlit)](https://book-recommender-model-haziumxyz.streamlit.app/)

---
## What It Does

BookMatch supports two types of users:

**I'm new to reading** — Users who haven't read many books select genres they think they might enjoy. The system recommends top-rated books within those genres, ranked by a weighted combination of average rating and popularity.

**I've read some books** — Users who have read books before search and select titles they've enjoyed. The system finds users with similar reading tastes and uses a trained SVD model to predict and rank books they haven't read yet.

---

## How It Works

### Content-Based (New Readers)
Books are scored using a weighted formula:

```
score = 0.7 × avg_rating + 0.3 × log(1 + num_ratings)
```

This balances rating quality against popularity, preventing obscure highly-rated books from dominating results.

### Collaborative Filtering (Returning Readers)
Built on the [Surprise](https://surpriselib.com/) library using SVD (Singular Value Decomposition). The model was trained on 90,556 explicit ratings from 6,837 users across 5,441 books. It learns latent factors — hidden patterns in user preferences and book characteristics — and uses them to predict how much a user would enjoy an unseen book.

**RMSE: 1.56** on a 1–10 rating scale.

### Genre Classification
Book genres were classified using the Groq API (llama-3.3-70b-versatile) based on each book's title and author. Results were validated and merged across multiple classification runs to maximise coverage.

---

## Dataset

[Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) — Books Crossing dataset containing 271,360 books, 278,858 users, and 1,149,780 ratings.

**Preprocessing:**
- Removed implicit ratings (rating = 0)
- Filtered to users with 10+ ratings and books with 10+ ratings
- Final working set: 5,441 books and 6,837 users

---

## Tech Stack

- **Python** — pandas, numpy, scikit-surprise, joblib
- **Groq API** — LLM-based genre classification
- **Streamlit** — web app interface
- **Open Library** — book cover images and book detail pages

---

## Project Structure

```
book_recommender/
├── app.py                  # Streamlit UI
├── train.py                # Genre classification script & Model training (run once)
├── recommender/
│   ├── collaborative.py    # SVD-based recommendation logic
│   ├── content.py          # Genre-based recommendation logic
│   └── utils.py            # Data loading and shared helpers
├── data/                   # CSVs (not tracked in git)
├── models/                 # Saved SVD model (not tracked in git)
└── requirements.txt
```

---

## Run Locally

**1. Clone the repo and install dependencies**
```bash
git clone https://github.com/Alao-Muizah/book-recommender
cd book-recommender
pip install -r requirements.txt
```

**2. Download the dataset**

Download from [Kaggle](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) and place `Books.csv`, `Ratings.csv`, and `Users.csv` in the `data/` folder.

**3. Classify genres** *(requires Groq API key)*
```bash
# Inside train.py
client = Groq(api_key="API_KEY")
# replace API_KEY with your own API KEY
```

**4. Train the model**
```bash
python train.py
```

**5. Run the app**
```bash
streamlit run app.py
```

---

## Notes

- Genre classification requires a [Groq API key](https://console.groq.com/). Add it to `train.py` before running.

- Book covers and detail pages are sourced from [Open Library](https://openlibrary.org/).
