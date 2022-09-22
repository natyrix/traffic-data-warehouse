from sqlalchemy import create_engine
import pandas as pd
import os
from datetime import timedelta,datetime
import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator

 
default_args = {
    'owner':'natnaelM',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

def load_raw_data(path, table_name):
    print("WRITING DATA")
    # engine = create_engine("postgresql+pygresql://airflow:airflow@host:5432/airflow")
    engine = create_engine("mysql+pymysql://root:@localhost/airflow")
    df = pd.read_csv(path, sep="[,;:]", index_col=False)
    # df1 = df
    # df = df1.iloc[:, :10]
    
    df.to_sql(table_name, con=engine, if_exists='replace',index_label='id')
    print("DATA SAVED")
 

with DAG(
    dag_id='dag_data',
    default_args=default_args,
    description='this dag loads raw data to ware house',
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval='@once'
)as dag:
    task1 = PythonOperator(
        task_id='migrate',
        python_callable=load_raw_data,
        op_kwargs={
            "path": "./data/raw_dataset.csv",
            "table_name":"trafficinfo"
        }
    )
    task1