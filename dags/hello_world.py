from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.models import Variable
import json

TEST = Variable.get("test", deserialize_json=True)

def helloWorld(**context):
    print(context['execution_date'])
    print('Hello World')
    print(TEST)
    print(type(TEST))

with DAG(dag_id="hello_world_dag",
         start_date=datetime(2021,1,1),
         schedule_interval="@hourly",
         catchup=False) as dag:
        
        task1 = PythonOperator(task_id="hello_world", python_callable=helloWorld, provide_context=True)

task1