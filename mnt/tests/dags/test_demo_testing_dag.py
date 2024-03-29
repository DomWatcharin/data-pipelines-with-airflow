from datetime import timedelta

from airflow import DAG
from airflow.utils.dag_cycle_tester import check_cycle

from demo_testing_dag import dag as demo_testing_dag_instance

# First test cycle
def test_demo_testing_dag_cycle():
    assert isinstance(demo_testing_dag_instance, DAG)
    check_cycle(demo_testing_dag_instance)

# Second test args
def test_demo_testing_dag_args():
    assert demo_testing_dag_instance.catchup is False
    assert demo_testing_dag_instance.default_args.get("owner") == "domwatcharin"
    assert demo_testing_dag_instance.default_args.get("retries") == 3
    assert demo_testing_dag_instance.default_args.get("retry_delay") == timedelta(minutes=3)



# pip install pytest
# export PYTHONPATH=/opt/airflow/plugins
# pytest