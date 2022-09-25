from datetime import timedelta,datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
import logging
log: logging.log = logging.getLogger("airflow")
log.setLevel(logging.INFO)

default_args={
    'owner':'NatnaelM',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

def modify_raw_data(location):
    updated_lines=""
    with open(location, 'r', encoding='ISO-8859-1') as f:
        lines = f.readlines()
        for index , line in enumerate(lines):
            each_line = line.split(';')
            if index != 0:
                updated_lines += ";".join(each_line[0:10]) + ";" + "_".join(each_line[10:])
            else:
                updated_lines += ";".join(each_line[:len(each_line)-1]) + ";" + "time" + ";" + "other_data" + "\n" 
    with open('./data/transformed_dataset', "w") as f:
        f.writelines(updated_lines)


with DAG(
    dag_id='load_raw_data_to_db',
    default_args=default_args,
    description='extract and load raw data to db',
    start_date=datetime(2022,9,21),
    schedule_interval='@once'
)as dag:
    task1 = PythonOperator(
        task_id='migrate',
        python_callable=modify_raw_data,
        op_kwargs={
            "location": "./data/raw_dataset.csv"
        }
    )
    task2 = PostgresOperator(
        task_id='create_database',
        postgres_conn_id='postgres_default',
        sql='/sql/init_db.sql',
    )
    task3 = PostgresOperator(
        task_id='create_dataset_table',
        postgres_conn_id='postgres_default',
        sql='/sql/raw_data.sql',
    )
    task4 = PostgresOperator(
        task_id='load_dataset',
        postgres_conn_id='postgres_default',
        sql='/sql/load_raw_data.sql',
    )

    task1 >> task2 >> task3 >> task4