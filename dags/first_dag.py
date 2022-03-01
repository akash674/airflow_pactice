from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(5),
    'email': ['akashdhakad546@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

my_first_dag = DAG(
    'first_dag',
    default_args=default_args,
    description='Our first DAG',
    schedule_interval=timedelta(days=1),
)

task_1 = BashOperator(
    task_id='first_task',
    bash_command='echo 1',
    dag=my_first_dag,
)

task_2 = BashOperator(
    task_id='second_task',
    bash_command='echo 2',
    dag=my_first_dag,
)

task_1.set_downstream(task_2)

airflow backfill my_first_dag -s 2022-03-01 -e 2022-03-05