import logging

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils import timezone

from operators.greeting import GreetingOperator


#def _greeting(greeting, name):
#    logging.info(f"{greeting}, {name}")


default_args = {
    "owner": "domwatcharin",
    "start_date": timezone.datetime(2022, 2, 1),
}
with DAG(
    "demo_custom_operator",
    default_args=default_args,
    schedule_interval=None,
) as dag:

    """greeting1 = PythonOperator(
        task_id="greeting1",
        python_callable=_greeting,
        op_kwargs={
            "greeting": "Hello",
            "name": "World"
        },
    )"""

    greeting1 = GreetingOperator(
        task_id="greting1",
        greeting="Hello",
        name="World",
    )

    """greeting2 = PythonOperator(
        task_id="greeting2",
        python_callable=_greeting,
        op_kwargs={
            "greeting": "Hey",
            "name": "Dom"
        },
    )"""

    greeting2 = GreetingOperator(
        task_id="greting2",
        greeting="Hey",
        name="Dom",
    )

    greeting1 >> greeting2