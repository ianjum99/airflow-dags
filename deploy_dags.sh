#!/bin/bash
scp -i <(echo "$SSH_KEY") airflow-dags/dags/*.py user@your-airflow-server:/path/to/airflow/dags
