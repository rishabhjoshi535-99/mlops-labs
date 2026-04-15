from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import logging

# Default arguments (PRODUCTION STYLE)
default_args = {
    'owner': 'rishabh',
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}

# Create DAG
with DAG(
    dag_id='simple_ml_pipeline',
    default_args=default_args,
    description='Simple ML pipeline using Airflow',
    schedule_interval='@daily',   # ✅ added
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    # TASK 1
    def load_data():
        logging.info("Loading data...")
        print("Data loaded successfully")

    # TASK 2
    def preprocess_data():
        logging.info("Preprocessing data...")
        print("Data preprocessed")

    # TASK 3
    def train_model():
        logging.info("Training model...")
        print("Model trained")

    # TASK 4
    def evaluate_model():
        logging.info("Evaluating model...")
        print("Model evaluated")

    # Operators
    load = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )

    preprocess = PythonOperator(
        task_id='preprocess_data',
        python_callable=preprocess_data
    )

    train = PythonOperator(
        task_id='train_model',
        python_callable=train_model
    )

    evaluate = PythonOperator(
        task_id='evaluate_model',
        python_callable=evaluate_model
    )

    # Task flow
    load >> preprocess >> train >> evaluate