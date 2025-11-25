from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import CustomerFeatures
import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path("models/churn_model.joblib")

app = FastAPI(
    title="Churn Prediction API",
    description="ML Classification Model using FastAPI + scikit-learn",
    version="1.0.0",
)

# ---------------------- CORS FIX ----------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # Allow all frontend origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ------------------------------------------------------

# Load model
model_artifact = joblib.load(MODEL_PATH)
model = model_artifact["model"]
feature_names = model_artifact["features"]

@app.get("/")
def home():
    return {"message": "Churn Prediction API running successfully!"}

@app.post("/predict")
def predict_churn(data: CustomerFeatures):

    data_dict = {
        "State": data.State,
        "Account length": data.Account_length,
        "Area code": data.Area_code,
        "International plan": data.International_plan,
        "Voice mail plan": data.Voice_mail_plan,
        "Number vmail messages": data.Number_vmail_messages,
        "Total day minutes": data.Total_day_minutes,
        "Total day calls": data.Total_day_calls,
        "Total day charge": data.Total_day_charge,
        "Total eve minutes": data.Total_eve_minutes,
        "Total eve calls": data.Total_eve_calls,
        "Total eve charge": data.Total_eve_charge,
        "Total night minutes": data.Total_night_minutes,
        "Total night calls": data.Total_night_calls,
        "Total night charge": data.Total_night_charge,
        "Total intl minutes": data.Total_intl_minutes,
        "Total intl calls": data.Total_intl_calls,
        "Total intl charge": data.Total_intl_charge,
        "Customer service calls": data.Customer_service_calls,
    }

    df = pd.DataFrame([data_dict])
    df = df[feature_names]

    pred = model.predict(df)[0]
    proba = model.predict_proba(df)[0][1]

    return {
        "churn": bool(pred),
        "churn_probability": float(proba)
    }
