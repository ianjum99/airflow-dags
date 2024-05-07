from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def extract():
    # Your logic to extract data
    pass

def transform():
    # Your logic to transform data
    pass

def load():
    # Your logic to load data into a destination
    pass

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email': ['example@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=10),
}

dag = DAG(
    'data_processing_pipeline',
    default_args=default_args,
    description='A simple data processing pipeline',
    schedule_interval='@daily',
)

t1 = PythonOperator(
    task_id='extract',
    python_callable=extract,
    dag=dag,
)

t2 = PythonOperator(
    task_id='transform',
    python_callable=transform,
    dag=dag,
)

t3 = PythonOperator(
    task_id='load',
    python_callable=load,
    dag=dag,
)

t1 >> t2 >> t3  # Define dependencies
