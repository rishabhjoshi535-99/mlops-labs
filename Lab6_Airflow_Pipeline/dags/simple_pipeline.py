from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Default arguments
default_args = {
    'owner': 'rishabh',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define DAG
dag = DAG(
    'simple_ml_pipeline',
    default_args=default_args,
    description='Simple ML pipeline using Airflow',
    schedule_interval=None,
    catchup=False,
)

# Task 1: Load Data
def load_data():
    print("Loading data...")

# Task 2: Preprocess Data
def preprocess_data():
    print("Preprocessing data...")

# Task 3: Train Model
def train_model():
    print("Training model...")

# Task 4: Evaluate Model
def evaluate_model():
    print("Evaluating model...")

# Create tasks
load = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

preprocess = PythonOperator(
    task_id='preprocess_data',
    python_callable=preprocess_data,
    dag=dag,
)

train = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag,
)

evaluate = PythonOperator(
    task_id='evaluate_model',
    python_callable=evaluate_model,
    dag=dag,
)

# Set dependencies
load >> preprocess >> train >> evaluate
