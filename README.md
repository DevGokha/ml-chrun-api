📊 Customer Churn Prediction — FastAPI + Machine Learning

This is the backend for the Customer Churn Prediction System, built using:

FastAPI for API development

Scikit-Learn for the machine learning model

Joblib for model serialization

Pydantic for input validation

The backend exposes an endpoint /predict that returns the churn probability for a telecom customer.

🚀 Features

✔ End-to-end ML pipeline
✔ Logistic Regression / Random Forest model
✔ Trained on Churn dataset
✔ Clean FastAPI structure
✔ Swagger docs (/docs)
✔ CORS enabled (supports frontend)
✔ Fast inference (model loaded once)

🧠 Prediction API
POST /predict
Request Body Example
{
  "State": "OH",
  "Account_length": 120,
  "Area_code": 415,
  "International_plan": "No",
  "Voice_mail_plan": "Yes",
  "Number_vmail_messages": 20,
  "Total_day_minutes": 120.5,
  "Total_day_calls": 110,
  "Total_day_charge": 20.48,
  "Total_eve_minutes": 150.2,
  "Total_eve_calls": 90,
  "Total_eve_charge": 15.50,
  "Total_night_minutes": 180.3,
  "Total_night_calls": 100,
  "Total_night_charge": 8.20,
  "Total_intl_minutes": 12.5,
  "Total_intl_calls": 3,
  "Total_intl_charge": 3.38,
  "Customer_service_calls": 2
}

Response Example
{
  "churn": false,
  "churn_probability": 0.21
}

🛠️ Installation & Setup
1️⃣ Create virtual environment
python -m venv venv

2️⃣ Activate environment
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Start server
uvicorn app.main:app --reload

API URLs

Swagger Docs → http://127.0.0.1:8000/docs

Root Endpoint → http://127.0.0.1:8000/

🔁 Train Your Own Model

To retrain:

python train_model.py


This generates:

models/churn_model.joblib

🧪 Tech Stack

Python

FastAPI

Scikit-Learn

Joblib

Pandas

Uvicorn

👤 Author

Dev Gokha
AI Engineer | MERN Stack Developer | Machine Learning Engineer
