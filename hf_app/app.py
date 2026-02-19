import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Hiring Probability Predictor")

Age = st.slider("Age", 18, 60, 30)
Gender = st.selectbox("Gender (0=female, 1=male)", [0, 1])
EducationLevel = st.slider("Education Level (1-4)", 1, 4, 2)
ExperienceYears = st.slider("Experience Years", 0, 20, 5)
PreviousCompanies = st.slider("Previous Companies", 0, 10, 2)
DistanceFromCompany = st.slider("Distance From Company", 0, 50, 10)
InterviewScore = st.slider("Interview Score", 0, 100, 70)
SkillScore = st.slider("Skill Score", 0, 100, 75)
PersonalityScore = st.slider("Personality Score", 0, 100, 70)
RecruitmentStrategy = st.slider("Recruitment Strategy (1-3)", 1, 3, 2)

if st.button("Predict"):

    data = np.array([[  
        Age,
        Gender,
        EducationLevel,
        ExperienceYears,
        PreviousCompanies,
        DistanceFromCompany,
        InterviewScore,
        SkillScore,
        PersonalityScore,
        RecruitmentStrategy
    ]])

    data_scaled = scaler.transform(data)
    proba = model.predict_proba(data_scaled)[0][1]

    st.success(f"Hiring probability: {proba*100:.2f}%")
