# main.py
from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
import requests

app = FastAPI()

scheduler = BackgroundScheduler()

@app.post("/scheduled_task")
def run_scheduled_task():
    # Логика вашей запланированной задачи
    response = requests.get("https://api.example.com/data")
    # Обработка полученных данных
    print("Запланированная задача выполнена.")
    return {"message": "Запланированная задача успешно выполнена"}

def scheduled_task():
    # Вызов POST-эндпоинта
    requests.post("http://your-server.com/scheduled_task")

# Настраиваем расписание
scheduler.add_job(id='scheduled_task', func=scheduled_task, trigger='cron', minute=0, hour=7, day=1)
scheduler.start()

@app.get("/")
def root():
    return {"message": "Приложение работает"}