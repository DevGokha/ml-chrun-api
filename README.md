# Customer Churn Prediction API

A lightweight backend API for predicting customer churn (telecom) built with FastAPI and scikit-learn. The service loads a pre-trained model and exposes a /predict endpoint that returns the churn probability for a customer.

Features
- End-to-end ML inference API
- Trained model serialized with joblib
- FastAPI routes with automatic Swagger UI (/docs)
- Input validation with Pydantic
- CORS enabled for frontend integration
- Model loaded once for fast inference

Table of contents
- [Demo](#demo)
- [API](#api)
- [Request / Response Examples](#request--response-examples)
- [Installation](#installation)
- [Running the server](#running-the-server)
- [Train your own model](#train-your-own-model)
- [Project structure](#project-structure)
- [Tech stack](#tech-stack)
- [Author](#author)
- [License](#license)

Demo
- Swagger UI: http://127.0.0.1:8000/docs
- Root endpoint: http://127.0.0.1:8000/

API
POST /predict
- Accepts a JSON payload describing customer features.
- Returns JSON with:
  - churn (boolean): predicted class (True if predicted to churn)
  - churn_probability (float): probability of churn (0.0 - 1.0)

Request / Response Examples

Sample request body:
```json
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
```

Sample response:
```json
{
  "churn": false,
  "churn_probability": 0.21
}
```

Installation

Prerequisites
- Python 3.8+ recommended
- git (optional)

1) Clone the repository (or download)
```bash
git clone https://github.com/DevGokha/ml-chrun-api.git
cd ml-chrun-api
```

2) Create a virtual environment
- Windows:
```powershell
python -m venv venv
venv\Scripts\Activate.ps1   # or venv\Scripts\activate
```
- macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

3) Install dependencies
```bash
pip install -r requirements.txt
```

Running the server (development)
```bash
uvicorn app.main:app --reload
```
Server will be available at http://127.0.0.1:8000/

Train your own model
If you want to retrain the model using the included training script:
```bash
python train_model.py
```
This script saves the trained model to:
- models/churn_model.joblib

Make sure any required training data is present and that any preprocessing steps align with what the API expects.

Project structure (example)
- app/
  - main.py           # FastAPI app and routes
  - schemas.py
- data/
  - churn-bigml-80.csv 
- models/
  - churn_model.joblib
- inspect_data.py 
- train_model.py
- requirements.txt
- README.md

Notes and tips
- The API expects features in the same format used during training; ensure categorical values and numeric scaling match.
- For production deployments, replace the development Uvicorn command with an ASGI server configuration (e.g., Gunicorn + Uvicorn workers or Uvicorn + process manager).
- Consider adding health and metrics endpoints for monitoring.

Tech stack
- Python
- FastAPI
- Scikit-Learn
- Joblib
- Pandas
- Uvicorn

Author
Dev Gokha
AI Engineer | MERN Stack Developer | Machine Learning Engineer

