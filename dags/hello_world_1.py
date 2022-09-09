from airflow import DAG
import airflow
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.models import Variable
import json

TEST = Variable.get("test1", deserialize_json=True)

def helloWorld(**context):
    print(context['key1'])
    print(context['key2'])
    print(context['execution_date'])
    print('Hello World')
    print(TEST)
    print(type(TEST))

with DAG(dag_id="hello_world_dag_1",
         start_date=airflow.utils.dates.days_ago(1),
         schedule_interval="@hourly",
         catchup=False) as dag:
        
        task1 = PythonOperator(task_id="hello_world", python_callable=helloWorld, provide_context=True, op_kwargs={'key1': 'value1', 'key2': 'value2'})

task1