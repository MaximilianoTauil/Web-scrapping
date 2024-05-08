import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.datetime(2024, 5, 10),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
}

dag = DAG(
    'mi_dag',
    default_args=default_args,
    description='Dag de actualizar datos',
    schedule_interval='01 18 * * *', # Ejecutar una vez al día
)

actualizar_datos = BashOperator(
    task_id='actualizar_datos',
    bash_command='python web_scrap.py',  # Ruta al script de Python para actualizar datos
    dag=dag,
)

iniciar_streamlit = BashOperator(
    task_id='iniciar_streamlit',
    bash_command='streamlit run app.py',  # Ruta al script de Streamlit
    dag=dag,
)

push_to_git = BashOperator(
    task_id='push_to_git',
    python_callable='Pushear.py',
    dag=dag,
)

actualizar_datos >> push_to_git >> iniciar_streamlit
