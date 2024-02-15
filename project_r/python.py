
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

# Define default_args dictionary to specify the default parameters of the DAG
default_args = {
    'owner': 'your_name',
    'start_date': datetime(2023, 1, 1),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate a DAG with the defined default_args
dag = DAG(
    'sample_dag',
    default_args=default_args,
    description='A simple Airflow DAG with 5 tasks',
    schedule_interval=timedelta(days=1),  # Run the DAG daily
)

# Task 1: Start the DAG
start_task = DummyOperator(
    task_id='start_task',
    dag=dag,
)

# Task 2: PythonOperator to execute a Python function
def task_two_function(**kwargs):
    print("Executing Task 2")
    # Add your logic here

task_two = PythonOperator(
    task_id='task_two',
    python_callable=task_two_function,
    provide_context=True,
    dag=dag,
)

# Task 3: Another PythonOperator
def task_three_function(**kwargs):
    print("Executing Task 3")
    # Add your logic here

task_three = PythonOperator(
    task_id='task_three',
    python_callable=task_three_function,
    provide_context=True,
    dag=dag,
)

# Task 4: DummyOperator
dummy_task = DummyOperator(
    task_id='dummy_task',
    dag=dag,
)

# Task 5: End the DAG
