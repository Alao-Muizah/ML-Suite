def recommend_tutors(
    tutors,
    student_profile=None
):
    """
    Recommend tutors for a student based on their profile.
    Returns a list of tutors with dynamic score.
    """
    if student_profile is None:
        student_profile = {}

    recommendations = []

    experience_weight_map = {"Beginner": 1, "Intermediate": 2, "Expert": 3}

    for tutor in tutors:
        # SUBJECT
        subject_pref = student_profile.get("subject")
        if subject_pref:
            tutor_subjects = [s.strip().lower() for s in tutor["subject"].split("|")]
            if subject_pref.lower() not in tutor_subjects:
                continue

        # LANGUAGE
        lang_pref = student_profile.get("language")
        if lang_pref:
            tutor_languages = [l.strip().lower() for l in tutor["language"].split("|")]
            if lang_pref.lower() not in tutor_languages:
                continue

        # TEACHING MODE
        mode_pref = student_profile.get("teaching_mode")
        if mode_pref and tutor["teaching_mode"].lower() != mode_pref.lower():
            continue

        # AVAILABILITY
        avail_pref = student_profile.get("availability")
        if avail_pref:
            tutor_avail = [a.strip().lower() for a in tutor["availability"].split("|")]
            if avail_pref.lower() not in tutor_avail:
                continue

        # EXPERIENCE LEVEL
        exp_pref = student_profile.get("experience_level")
        if exp_pref and tutor["experience_level"].lower() != exp_pref.lower():
            continue

        # CERTIFICATION
        cert_pref = student_profile.get("certification")
        if cert_pref and tutor["certification"].lower() != cert_pref.lower():
            continue

        # PRICE
        max_price = student_profile.get("max_price")
        price_score = 0
        if max_price is not None:
            if tutor["price"] == 0 or tutor["price"] <= max_price:
                price_score = 1
            else:
                continue
        # GENDER
        gender_pref = student_profile.get("gender")
        if gender_pref and tutor["gender"].lower() != gender_pref.lower():
            continue

        # SCORE CALCULATION
        exp_score = experience_weight_map[tutor["experience_level"]] / 3
        rating_score = tutor["rating"] / 5
        availability_score = 1  # already filtered, counts as 1

        score = (exp_score * 0.4) + (rating_score * 0.4) + (availability_score * 0.1) + (price_score * 0.1)

        recommendations.append({
            "tutor_id": tutor["tutor_id"],
            "gender": tutor["gender"],
            "subject": [s.strip() for s in tutor["subject"].split("|")],
            "teaching_mode": tutor["teaching_mode"],
            "language": [l.strip() for l in tutor["language"].split("|")],
            "price": tutor["price"],
            "availability": [a.strip() for a in tutor["availability"].split("|")],
            "experience_level": tutor["experience_level"],
            "certification": tutor["certification"],
            "rating": tutor["rating"],
            "score": score
        })

    # Sort descending by score
    recommendations.sort(key=lambda x: x["score"], reverse=True)

    return recommendations