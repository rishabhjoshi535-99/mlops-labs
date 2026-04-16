# Lab 3 - FastAPI ML Model Deployment

## Objective
Deploy a machine learning model using FastAPI.

## Steps Performed
- Trained Iris classification model using scikit-learn
- Saved model using joblib
- Created FastAPI application
- Built /predict endpoint for inference
- Tested API using Swagger UI

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Train model:
python3 train_model.py

3. Run API:
uvicorn app:app --reload

4. Open in browser:
http://127.0.0.1:8000/docs

## Sample Input
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}

## Output
{
  "prediction": 0
}
