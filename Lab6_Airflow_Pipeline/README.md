# Lab 6 – Airflow Pipeline

## Overview

This lab demonstrates how to build and run a simple Machine Learning pipeline using Apache Airflow. The pipeline is implemented as a Directed Acyclic Graph (DAG) and executed using Docker.

---

## Objective

- Understand Airflow DAG structure
- Build a multi-step ML pipeline
- Execute and monitor workflows using Airflow UI
- Implement scheduling, retries, and logging for production readiness

---

## Tech Stack

- Python
- Apache Airflow
- Docker
- PostgreSQL

---

## Project Structure

```
Lab6_Airflow_Pipeline/
├── dags/
│   └── simple_ml_pipeline.py
├── docker-compose.yaml
├── requirements.txt
└── README.md
```

---

## Pipeline Workflow

The DAG consists of the following sequential tasks:

1. **load_data** – Loads dataset
2. **preprocess_data** – Cleans and prepares data
3. **train_model** – Trains machine learning model
4. **evaluate_model** – Evaluates model performance

---

## DAG Features (Production Enhancements)

- **Scheduling:** Runs automatically using `@daily`
- **Retries:** 2 retries for fault tolerance
- **Logging:** Tracks execution using Python logging
- **Orchestration:** Task dependencies managed via DAG

---

## How to Run

**Step 1: Start Docker containers**
```bash
docker compose up
```

**Step 2: Initialize Airflow database**
```bash
docker compose run airflow-webserver airflow db init
```

**Step 3: Access Airflow UI**

Open in browser: [http://localhost:8080](http://localhost:8080)

**Step 4: Run the DAG**

- Enable DAG (`simple_ml_pipeline`)
- Click **Trigger**
- Monitor execution in **Graph view**

---

## Results

- DAG executed successfully
- All tasks completed without errors
- Workflow visualized and monitored via Airflow UI
- Multiple scheduled runs observed

---

## Conclusion

Apache Airflow enables efficient orchestration of machine learning pipelines through DAG-based workflows. The addition of scheduling, retries, and logging makes the pipeline more robust and production-ready.
