import logging

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils import timezone


def _hello():
    logging.info("Hello")


default_args = {
    "owner": "domwatcharin",
    "start_date": timezone.datetime(2024, 1, 1),
}
with DAG(
    "demo_operators", #same with file name
    default_args=default_args,
    schedule_interval=None, 
) as dag:

    hello = PythonOperator(
        task_id="hello", # same with task instant
        python_callable=_hello, # same with fuction
    )
