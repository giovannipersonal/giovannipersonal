from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime,timedelta

defaultArgs = {
    'depends_on_past' : False,
    'start_date' : datetime(2023,4,27),
    'email' : ['giovanni.nolasco@vetta.digital'],
    'email_on_failure' : False,
    'email_on_retry' : False,
    'retries': 1,
    'retry_delay' : timedelta(seconds=10)
}

dag = DAG('DefaultArgsDAG', description="dag de Trigger de Dag", 
        default_args=defaultArgs,
        schedule_interval='@hourly', start_date = datetime(2023,5,11), 
        catchup=False, default_view='graph', tags=['processo','pipeline'])

task1 = BashOperator(task_id="tsk1", bash_command="sleep 5", dag=dag )
task2 = BashOperator(task_id="tsk2", bash_command="sleep 5", dag=dag )



task1 >> task2