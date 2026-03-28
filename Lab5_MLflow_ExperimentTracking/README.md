# Lab 5 – MLflow Experiment Tracking

## Overview
This lab demonstrates how to use MLflow for experiment tracking in a simple machine learning workflow. A linear regression model is trained and tracked using MLflow.

## Objective
The goal of this lab is to:
- Track machine learning experiments using MLflow
- Log parameters, metrics, and models
- Understand MLflow experiment and run structure

## Tech Stack
- Python
- scikit-learn
- MLflow
- NumPy

## Implementation

### 1. Dataset
A small custom dataset is created using NumPy:
- Input: X = [[1], [2], [3], [4], [5], [6]]
- Output: y = [3, 5, 7, 9, 11, 13]

### 2. Model
- Linear Regression model from scikit-learn

### 3. MLflow Tracking
The following are logged:
- Parameters:
  - model_type
  - dataset_size
- Metrics:
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)
- Model:
  - Trained regression model

### 4. Experiment Details
- Experiment Name: Lab5_LinearRegression_Experiment
- Run Name: LinearRegression_Run

## How to Run

1. Install dependencies:
```bash
pip install mlflow scikit-learn numpy
```

2. Run the script:
```bash
python3 src/linear_regression.py
```

3. Start MLflow UI:
```bash
mlflow ui
```

4. Open browser:
```bash
http://127.0.0.1:5000
```

## Output
- MLflow UI displays:
  - Experiment
  - Run details
  - Metrics and parameters
  - Model artifact

## Conclusion
This lab successfully demonstrates how MLflow can be used to track machine learning experiments and manage model outputs in a structured way.
