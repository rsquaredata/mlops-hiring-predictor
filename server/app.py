from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from pymongo import MongoClient

app = FastAPI()

# Load ML
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Connect Mongo
client = MongoClient("mongodb://mongo:27017")
db = client["mlops_db"]
collection = db["predictions"]


class Candidate(BaseModel):
    Age: float
    Gender: float
    EducationLevel: float
    ExperienceYears: float
    PreviousCompanies: float
    DistanceFromCompany: float
    InterviewScore: float
    SkillScore: float
    PersonalityScore: float
    RecruitmentStrategy: float


@app.post("/predict")
def predict(candidate: Candidate):

    data = np.array([[  
        candidate.Age,
        candidate.Gender,
        candidate.EducationLevel,
        candidate.ExperienceYears,
        candidate.PreviousCompanies,
        candidate.DistanceFromCompany,
        candidate.InterviewScore,
        candidate.SkillScore,
        candidate.PersonalityScore,
        candidate.RecruitmentStrategy
    ]])

    data_scaled = scaler.transform(data)
    proba = float(model.predict_proba(data_scaled)[0][1])

    record = candidate.dict()
    record["hiring_probability"] = proba

    collection.insert_one(record)

    return {
        "hiring_probability": round(proba, 4)
    }


@app.get("/history")
def get_history():
    results = list(collection.find({}, {"_id": 0}))
    return {"results": results}
