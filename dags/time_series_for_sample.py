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

def transform_data():
    cols = ['track_id', 'type', 'lat', 'lng', 'speed', 'lon_acc', 'lat_acc', 'time']

    with open("./data/sample.csv", 'r', encoding='ISO-8859-1') as f:
        lines = f.readlines()
        updated_lines=""
        for index , line in enumerate(lines):
            # if index == 2:
            #     break
            each_line = line.split(';')
            if index != 0:
                new_lines = [l.strip() for l in each_line]
                other_data = new_lines[4:]
                i=0
                while i < len(other_data):
                    vals = other_data[i:i+6]
                    i+=84
                    # if i < 1000:
                    if len(vals) != 0:
                        x = [new_lines[0], new_lines[1]]
                        for v in vals:
                            x.append(v)
                        if len(x)==8:
                            updated_lines += ";".join(x) +"\n"
                    else:
                        break
            else:
                new_lines = [l.strip() for l in each_line]
                updated_lines += ";".join(cols) + "\n" 

    with open('./data/time_series_transformed_dataset.csv', "w") as f:
        f.writelines(updated_lines)

def load_data_to_db(path, table_name):
    print("WRITING DATA")
    engine = create_engine("postgresql+postgresql://postgres:nvskFr7xOO8bndqdqh9W@containers-us-west-30.railway.app:7828/railway")
    df = pd.read_csv(path, sep=";", index_col=False)

    df.to_sql(table_name, con=engine, if_exists='replace',index_label='id')
    print("DATA SAVED")

with DAG(
    dag_id='save_time_series_to_db',
    default_args=default_args,
    description='this dag sample time series data to db',
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval='@once'
)as dag:
    task1 = PythonOperator(
        task_id='transform_time_series',
        python_callable=transform_data
    )
    task2 = PythonOperator(
        task_id='save_time_series',
        python_callable=transform_data,
        op_kwargs={
            "path": "./data/time_series_transformed_dataset.csv",
            "table_name":"sample_time_series"
        }
    )
    task1 >> task2