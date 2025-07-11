#!/bin/bash

# Step 1: Install required Python packages
echo "Installing dependencies..."
pip install fastapi uvicorn pandas scikit-learn joblib --quiet

# Step 2: Launch the API server
echo "Starting the FastAPI server at http://127.0.0.1:8000 ..."
uvicorn churn_api:app --reload
