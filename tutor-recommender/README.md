# Overview
Built a high-performance Tutor Recommendation System to match students with the most suitable tutors based on multiple criteria such as subject, language, teaching mode, availability, experience level, certification, and price.  
The project focuses on delivering **personalized, dynamic recommendations** using a scoring algorithm and modular, maintainable Python code.

# Dataset
The dataset contains details of tutors including tutor ID, gender, subjects they teach, languages spoken, teaching mode, experience level, rating, availability, certification, and price.  
The dataset is stored in CSV format (`data/tutors.csv`) and includes a variety of tutors to simulate a real-world tutoring platform.

# Tools & Libraries
Python, Pandas, NumPy, Streamlit, FastAPI

# Approach & Methodology
- Loaded and processed the tutor dataset using **Python file handling and Pandas**  
- Explored tutor features and structured them for compatibility with the recommendation engine  
- Implemented **filtering logic** to match student preferences with tutor attributes (subject, language, teaching mode, etc.)  
- Designed a **dynamic scoring algorithm** combining tutor rating, experience, availability, and price  
- Built a **modular structure**:
  - `models/recommender.py` → recommendation logic  
  - `utils/data_loader.py` → data reading and processing functions  
- Created a **Streamlit web app** for interactive student input  
- Developed a **FastAPI backend** exposing endpoints to fetch ranked tutor recommendations  

# Model Evaluation / Recommendations
- Tutors are scored based on:
  - **Experience level** (weighted)  
  - **Rating** (scaled to 0–1)  
  - **Availability match**  
  - **Price suitability**  
- Recommendations are returned **ranked by score**, ensuring the top tutors best match student preferences.  
- Example: A student preferring online Mathematics tutors under $5000 receives a sorted list of tutors with scores ranging from 0–1, maximizing relevance.

# Dataset Link
[Download tutors.csv](data/tutors.csv)  

# Streamlit Web App
[Open Tutor Recommender App](https://deen-app-recommender-haziumxyzqr.streamlit.app/)  



