from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email': ['example@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'daily_database_backup',
    default_args=default_args,
    description='A simple DAG to backup database daily',
    schedule_interval=timedelta(days=1),
)

t1 = BashOperator(
    task_id='backup_database_task',
    bash_command='pg_dump -h localhost -U postgres db_name > /path/to/your/backups/db_backup_$(date +%Y-%m-%d).sql',
    dag=dag,
)
