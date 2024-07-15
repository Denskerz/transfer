# app.py
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI приложение запущено!"}

def run_app():
    uvicorn.run(app, host="0.0.0.0", port=8000)

# scheduler.py
import schedule
import time
from datetime import datetime

def scheduled_task():
    # Проверяем, является ли текущий день 5-м числом месяца
    if datetime.now().day == 5:
        # Код вашей запланированной задачи
        print("Запланированная задача выполнена!")

def run_scheduler():
    # Настраиваем расписание на 7:00 каждого 5-го числа месяца
    schedule.every().day.at("07:00").do(scheduled_task)

    # Запускаем цикл для выполнения запланированных задач
    while True:
        schedule.run_pending()
        time.sleep(1)

# main.py
if __name__ == "__main__":
    import threading

    # Запускаем FastAPI приложение в новом потоке
    app_thread = threading.Thread(target=run_app)
    app_thread.start()

    # Запускаем планировщик задач в основном потоке
    run_scheduler()