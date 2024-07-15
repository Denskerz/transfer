import schedule
import time
from datetime import datetime, date, timedelta

def task_at_start_of_previous_month():
    # Получаем дату первого числа прошлого месяца
    today = date.today()
    first_of_previous_month = date(today.year, today.month, 1) - timedelta(days=1)
    first_of_previous_month = first_of_previous_month.replace(day=1)

    print(f"Эта задача выполняется в начале предыдущего месяца - {first_of_previous_month.strftime('%B %Y')}")

# Запланируйте выполнение задачи в первый день каждого месяца
schedule.every().month.do(task_at_start_of_previous_month).tag("start_of_previous_month")

# Главный цикл, который будет проверять и выполнять запланированные задачи
while True:
    schedule.run_pending()

    # Проверяем, что сегодня - первое число
    if date.today().day == 1:
        schedule.run_all(tag="start_of_previous_month")

    time.sleep(1)
