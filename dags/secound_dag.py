from datetime import datetime
from airflow import models
from airflow.operators.bash_operator import BashOperator

yesterday = datetime.datetime.combine(
   datetime.datetime.today() - datetime.timedelta(1),
   datetime.datetime.min.time())

default_dag_args = {
    'start_date': yesterday,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
    'project_id': models.Variable.get('gcp_project')
}

with models.DAG(
        ‘Bash_operations’,
        schedule_interval=datetime.timedelta(days=1),
        default_args=default_dag_args) as dag:


t1 = BashOperator(
	task_id=’Make directory’, bash_command=’mkdir folder_name’, dag=dag)


t2 = BashOperator(
	task_id=’delete directory’, bash_command=’rm -rf folder_name’, dag=dag)

t1 >> t2   # This is how we set dependency among two tasks