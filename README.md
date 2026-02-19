# MLOps Hiring Predictor

A dockerized microservices application for predicting hiring decisions
using a machine learning model.

This project implements a complete MLOps pipeline including:

-   Data preprocessing and model training (scikit-learn)
-   Model serialization (joblib)
-   FastAPI REST API for inference
-   Streamlit frontend interface
-   MongoDB for prediction logging
-   Docker & Docker Compose orchestration

------------------------------------------------------------------------

## Architecture

Browser → Streamlit (client)\
        ↓\
     FastAPI (server)\
        ↓\
     MongoDB (database)

-   The client sends candidate features to the API.
-   The server loads a trained model and returns a hiring probability.
-   Each prediction is stored in MongoDB.

------------------------------------------------------------------------

## Dataset

The model is trained on the Kaggle dataset:

**Predicting Hiring Decisions in Recruitment Data**

The dataset contains candidate features such as:

-   Age
-   EducationLevel
-   ExperienceYears
-   InterviewScore
-   SkillScore
-   PersonalityScore
-   RecruitmentStrategy

Target variable:

-   HiringDecision (0 / 1)

The dataset presents moderate class imbalance (\~69% / 31%).

------------------------------------------------------------------------

## Model

-   Algorithm: Logistic Regression
-   Features scaled using StandardScaler
-   Trained using an 80/20 split
-   Final accuracy ≈ 0.87 on test set

The model returns a probability of hiring rather than a binary
classification.

------------------------------------------------------------------------

## Running the Project

From the root directory:

``` bash
docker compose up --build
```

Services:

-   FastAPI → http://localhost:8000/docs
-   Streamlit → http://localhost:8501

------------------------------------------------------------------------

## API Endpoints

### POST /predict

Returns hiring probability.

Example request:

``` json
{
  "Age": 30,
  "Gender": 1,
  "EducationLevel": 3,
  "ExperienceYears": 5,
  "PreviousCompanies": 2,
  "DistanceFromCompany": 10,
  "InterviewScore": 80,
  "SkillScore": 75,
  "PersonalityScore": 70,
  "RecruitmentStrategy": 2
}
```

Response:

``` json
{
  "hiring_probability": 0.6087
}
```

------------------------------------------------------------------------

### GET /history

Returns stored predictions from MongoDB.

------------------------------------------------------------------------

## Project Structure

    mlops-hiring-predictor/
    │
    ├── client/
    │   ├── app.py
    │   ├── Dockerfile
    │   └── requirements.txt
    │
    ├── server/
    │   ├── app.py
    │   ├── train.py
    │   ├── model.pkl
    │   ├── scaler.pkl
    │   ├── Dockerfile
    │   └── requirements.txt
    │
    ├── docker-compose.yml
    └── README.md

------------------------------------------------------------------------

## Notes

-   The dataset is used for educational and demonstration purposes.
-   This project demonstrates end-to-end containerized ML deployment.
