from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from datetime import datetime
import os

# Функция для получения файлов
def get_files(**kwargs):
    folder_path = '/path/to/your/folder'
    files = os.listdir(folder_path)
    return [os.path.join(folder_path, file) for file in files]

# DAG
with DAG('send_files_dag', start_date=datetime(2023, 1, 1), schedule_interval='@daily') as dag:
    
    get_files_task = PythonOperator(
        task_id='get_files',
        python_callable=get_files,
        provide_context=True,
    )

    send_email_task = EmailOperator(
        task_id='send_email',
        to='recipient@example.com',
        subject='Files from folder',
        html_content='Please find the attached files.',
        files=get_files_task.output,
    )

    get_files_task >> send_email_task



