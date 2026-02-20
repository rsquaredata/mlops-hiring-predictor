<div align="center">
  
# MLOps Hiring - Core
## (Local Development & Training Environment)

</div> 
This repository contains the local full-stack development environment for the MLOps Hiring system.

It serves as:

- 🧠 Model training environment
- 🐳 Docker Compose orchestration layer
- 🧪 Local API & UI testing
- 🗄️ Local MongoDB logging
- 📦 Model artifact generation for production deployment

---

## Role in the Global Architecture

This repository represents the **development layer** of the system.

Production deployment is handled in separate repositories:

- Backend API → HuggingFace Space
- Frontend UI → HuggingFace Space
- MongoDB Atlas → Cloud database

---

## Machine Learning Pipeline

- Dataset: [Kaggle - *Predicting Hiring Decisions in Recruitment Data*](https://www.kaggle.com/datasets/rabieelkharoua/predicting-hiring-decisions-in-recruitment-data)
- Preprocessing with `StandardScaler`
- Logistic Regression (class imbalance handled)
- Train/test split: 80/20
- Probability-based inference
- Model serialized via `joblib`

Artifacts generated:

- `model.pkl`
- `scaler.pkl`

These artifacts are used in production backend deployment.

---

## Local Full-Stack Environment

Run the entire stack locally:

```bash
docker compose up --build
```

---

## Services:

FastAPI → http://localhost:8000/docs

Streamlit → http://localhost:8501

MongoDB → local container

---

## Local Architecture

```
Browser
↓
Streamlit (client container)
↓
FastAPI (server container)
↓
MongoDB (container)
```

---

## Project Structure

```
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
```

---

## Why This Repository Exists

This repository isolates:

- Local experimentation
- Model development
- Containerized service testing
- Reproducible dev environment
- Production deployment is handled separately with CI/CD and cloud infrastructure.

---

## Notes

This project is designed for educational and portfolio demonstration purposes.

It showcases a complete end-to-end MLOps workflow:  
training → containerization → API → UI → database → cloud deployment.

---

Go back to the [meta repository](https://github.com/rsquaredata/mlops-hiring).
