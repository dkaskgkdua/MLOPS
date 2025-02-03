from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# DAG 정의
default_args = {
    'owner': 'song',
    'depends_on_past': False,
    'email': ['<EMAIL>'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 12, 1),

}

dag = DAG(
    'hello_airflow_dag',
    default_args=default_args,
    description='our first time practice airflow',
    schedule_interval=timedelta(days=1),
)

sentence = "hello airflow dag. fast campus lecture! we can do it."

def print_word(word):
    print(word)

prev_task = None
for i, word in enumerate(sentence.split()):
    task = PythonOperator(
        task_id=f'print_word_{i}',
        python_callable=print_word,
        op_kwargs={'word': word},
        dag=dag,
    )

    if prev_task:
        prev_task >> task

    prev_task = task