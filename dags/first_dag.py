from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(
    'first_tag',
    description='A simple first',
    schedule_interval="5 4 * * *",
    start_date=datetime(2022,1,1),
    catchup=False,
    tags=['example'],
) as dag:
    @task(task_id='first_task')
    def prints_something():
        print("Hello World")
        return("Hello World")

    prints_something()
