from airflow.models import DagBag

def test_dag_loaded():
    dag_bag = DagBag(dag_folder='airflow-dags/dags/', include_examples=False)
    assert 'daily_database_backup' in dag_bag.dags
    assert len(dag_bag.import_errors) == 0, "DAGs failed to load"
