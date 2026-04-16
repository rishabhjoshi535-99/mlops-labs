from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize app
app = FastAPI()

# Load trained model
model = joblib.load("iris_model.pkl")


# Input schema
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# Health check endpoint
@app.get("/")
def home():
    return {"message": "Iris Prediction API is running"}


# Prediction endpoint
@app.post("/predict")
def predict(data: IrisInput):
    # Convert input to numpy array
    input_data = np.array([[ 
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    return {
        "prediction": int(prediction[0])
    }