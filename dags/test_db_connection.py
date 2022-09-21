from sqlalchemy import create_engine


engine = create_engine("postgresql+pygresql://airflow:airflow@host:5432/airflow")