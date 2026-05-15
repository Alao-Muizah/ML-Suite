# main.py
from fastapi import FastAPI, Query
from typing import Optional
from utils.data_loader import load_csv
from models.tutor_recommender import recommend_tutors

app = FastAPI(title="Deen Hub Tutor Recommender")

# Load tutors once at startup
tutors = load_csv("data/tutors.csv")

@app.get("/recommend_tutors")
def get_recommended_tutors(
    gender: Optional[str] = Query(None, description="Student's gender"),
    subject: Optional[str] = Query(None, description="Subject student wants to learn"),
    language: Optional[str] = Query(None, description="Preferred language"),
    teaching_mode: Optional[str] = Query(None, description="Virtual, Physical, Hybrid"),
    availability: Optional[str] = Query(None, description="Morning, Afternoon, Evening"),
    max_price: Optional[int] = Query(None, description="Maximum price student can pay")
):
    """
    Returns a list of recommended tutors for a student profile
    """
    student_profile = {
        "subject": subject,
        "gender":gender,
        "language": language,
        "teaching_mode": teaching_mode,
        "availability": availability,
        "max_price": max_price
    }

    # Remove None values
    student_profile = {k: v for k, v in student_profile.items() if v is not None}

    recommendations = recommend_tutors(tutors, student_profile)
    return {"recommended_tutors": recommendations}
