from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(
    title="Churn Prediction API",
    description="Predicts churn probability based on customer features",
    version="1.0"
)

# Load trained pipeline
model = joblib.load("churn_model_pipeline.pkl")

# Define input schema
class CustomerFeatures(BaseModel):
    feature1: float
    feature2: str
    feature3: float

@app.post("/predict")
def predict_churn(data: CustomerFeatures):
    df = pd.DataFrame([data.dict()])
    prob = model.predict_proba(df)[0, 1]
    prediction = model.predict(df)[0]
    return {
        "churn_probability": round(float(prob), 4),
        "predicted_class": int(prediction)
    }
