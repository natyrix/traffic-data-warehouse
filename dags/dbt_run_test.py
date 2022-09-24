from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import datetime
from airflow.utils.dates import timedelta

default_args={
    'owner':'NatnaelM',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

with DAG(
    dag_id='run_and_test_dbt',
    default_args=default_args,
    description='An Airflow DAG to invoke simple dbt commands',
    start_date=datetime(2022,9,21),
    schedule_interval='@once'
) as dag:
    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='dbt run --project-dir ../../opt/dbt/traffic_dbt --profiles-dir ../'
    )

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='dbt test'
    )

    dbt_run >> dbt_test

