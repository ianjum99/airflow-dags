# Importing necessary modules from airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


def log_message():
    print("This is a test log from the simple_logging_dag.")

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Defining the DAG
with DAG(
    'simple_logging_dag',
    default_args=default_args,
    description='A simple DAG that logs a message',
    schedule_interval=timedelta(days=1),
    catchup=False,
) as dag:

    # Task to log the message
    log_task = PythonOperator(
        task_id='log_message',
        python_callable=log_message,
    )

# Setting task sequence
log_task
