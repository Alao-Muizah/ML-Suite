# app.py
import streamlit as st
from utils.data_loader import load_csv
from models.tutor_recommender import recommend_tutors

# ----------------- Page Config -----------------
st.set_page_config(
    page_title="DeenHub Tutor Recommender",
    layout="wide"
)

st.title("📚 DeenHub AI Tutor Recommendation System")
st.write(
    "This demo shows how DeenHub recommends the most suitable tutors "
    "based on a student's preferences using AI-based scoring."
)

# ----------------- Load Data -----------------
tutors = load_csv("data/tutors.csv")

# ----------------- Helper Function -----------------
def get_unique_values(tutors, column):
    """
    Return a sorted list of unique values in the column.
    Splits by '|' if needed for multi-value columns.
    """
    unique = set()
    for tutor in tutors:
        val = tutor[column]
        if isinstance(val, str) and '|' in val:
            unique.update([v.strip() for v in val.split('|')])
        else:
            unique.add(val)
    return sorted(unique)

# ----------------- Sidebar Filters -----------------
st.sidebar.header("🎯 Student Preferences")

# Gender dropdown
gender_options = ["Any"] + get_unique_values(tutors, "gender")
gender = st.sidebar.selectbox("Preferred Tutor Gender", gender_options)

# Subject dropdown
subject_options = ["Any"] + get_unique_values(tutors, "subject")
subject = st.sidebar.selectbox("Subject", subject_options)

# Language dropdown
language_options = ["Any"] + get_unique_values(tutors, "language")
language = st.sidebar.selectbox("Preferred Language", language_options)

# Teaching mode dropdown
mode_options = ["Any"] + get_unique_values(tutors, "teaching_mode")
teaching_mode = st.sidebar.selectbox("Teaching Mode", mode_options)

# Availability dropdown
availability_options = ["Any"] + get_unique_values(tutors, "availability")
availability = st.sidebar.selectbox("Availability", availability_options)

# Max price slider
prices = [tutor["price"] for tutor in tutors if tutor["price"] > 0]
max_price = st.sidebar.slider(
    "Maximum Price (₦)",
    min_value=0,
    max_value=int(max(prices)),
    value=int(max(prices)/2),
    step=500
)

# ----------------- Build Student Profile -----------------
student_profile = {}
if gender != "Any":
    student_profile["gender"] = gender
if subject != "Any":
    student_profile["subject"] = subject
if language != "Any":
    student_profile["language"] = language
if teaching_mode != "Any":
    student_profile["teaching_mode"] = teaching_mode
if availability != "Any":
    student_profile["availability"] = availability

student_profile["max_price"] = max_price

# ----------------- Recommend Tutors -----------------
if st.button("🔍 Recommend Tutors"):
    results = recommend_tutors(tutors, student_profile)

    if not results:
        st.warning("No tutors match your preferences.")
    else:
        st.subheader("✅ Recommended Tutors")

        for tutor in results:
            with st.expander(f"Tutor #{tutor['tutor_id']} — Score: {tutor['score']:.2f}"):
                st.write(f"**Gender:** {tutor['gender']}")
                st.write(f"**Subjects:** {', '.join(tutor['subject'])}")
                st.write(f"**Languages:** {', '.join(tutor['language'])}")
                st.write(f"**Teaching Mode:** {tutor['teaching_mode']}")
                st.write(f"**Availability:** {', '.join(tutor['availability'])}")
                st.write(f"**Experience Level:** {tutor['experience_level']}")
                st.write(f"**Certification:** {tutor['certification']}")
                st.write(f"**Price:** ₦{tutor['price']}")
