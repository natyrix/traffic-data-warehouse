from datetime import timedelta,datetime
from airflow import DAG
import airflow
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from sqlalchemy import create_engine
import pandas as pd
import logging
log: logging.log = logging.getLogger("airflow")
log.setLevel(logging.INFO)

default_args={
    'owner':'NatnaelM',
    'retries':1,
    'retry_delay':timedelta(minutes=2)
}

def modify_data(location):
    print("TRANSFORMING")
    with open(location, 'r', encoding='ISO-8859-1') as f:
        lines = f.readlines()
        updated_lines=""
        for index , line in enumerate(lines):
            each_line = line.split(';')
            if index != 0:
                new_lines = [l.strip() for l in each_line]
                updated_lines += ";".join(new_lines[0:10]) + ";" + "_".join(new_lines[10:])+"\n"
            else:
                new_lines = [l.strip() for l in each_line]
                updated_lines += ";".join(new_lines[:len(new_lines)-1]) + ";" + "time" + ";" + "other_data" + "\n" 
    with open('./data/transformed_dataset.csv', "w") as f:
        f.writelines(updated_lines)
    print("TRANSFORMED")
    

def save_data(table_name):
    print("SAVING TO DB")
    engine = create_engine("postgresql://postgres:nvskFr7xOO8bndqdqh9W@containers-us-west-30.railway.app:7828/railway")
    df = pd.read_csv("./data/transformed_dataset.csv", sep=";", index_col=False)
    df.to_sql(table_name, con=engine, if_exists='replace',index_label='id')
    print("SAVED")


with DAG(
    dag_id='transform_and_save_to_db',
    default_args=default_args,
    description='this dag transforms and saves',
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval='@once'
)as dag:
    task1 = PythonOperator(
        task_id='modify_and_add',
        python_callable=modify_data,
        op_kwargs={
            "location": "./data/raw_dataset.csv"
        }
    )
    task2 = PythonOperator(
        task_id='save_modified',
        python_callable=save_data,
        op_kwargs={
            "table_name": "transformed_data"
        }
    )
    task1 >> task2

