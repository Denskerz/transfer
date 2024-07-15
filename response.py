# scheduler.py
import schedule
import time
from datetime import datetime
import logging

logging.basicConfig(level=logging.ERROR, filename="scheduler.log", filemode="a")

def scheduled_task():
    try:
        # Проверяем, является ли текущий день 5-м числом месяца
        if datetime.now().day == 5:
            # Код вашей запланированной задачи
            print("Запланированная задача выполнена!")
    except Exception as e:
        logging.error(f"Ошибка при выполнении запланированной задачи: {e}")

def run_scheduler():
    # Настраиваем расписание на 7:00 каждого 5-го числа месяца
    schedule.every().day.at("07:00").do(scheduled_task)

    # Запускаем цикл для выполнения запланированных задач
    while True:
        schedule.run_pending()
        time.sleep(1)