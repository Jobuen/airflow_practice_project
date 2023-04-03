from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from twitter_etl import run_twitter_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 3),
    'email': None,
    "email_on_failure": False,
    "email_on_retry": False,
    'retries': 1,
    "retry_delay": timedelta(minutes=2),
}

dag = DAG(
    "twitter_dag",
    default_args=default_args,
    description="A simple DAG"
)


run_etl = PythonOperator(
    task_id="test",
    python_callable=run_twitter_etl,
    dag=dag)
