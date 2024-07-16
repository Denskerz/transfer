# main.py
from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from scheduled_task import run_scheduled_task

app = FastAPI()

# Создаем экземпляр планировщика
scheduler = BackgroundScheduler()

# Функция, которая будет вызываться по расписанию
def scheduled_task():
    run_scheduled_task()

# Настраиваем расписание
scheduler.add_job(id='scheduled_task', func=scheduled_task, trigger='cron', minute=0, hour=7, day=1)
scheduler.start()

@app.get("/")
def root():
    return {"message": "Приложение работает"}