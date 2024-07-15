import schedule
import time
from datetime import datetime, date, timedelta

def task_at_start_of_previous_month():
    # Получаем дату первого числа прошлого месяца
    today = date.today()
    first_of_previous_month = date(today.year, today.month, 1) - timedelta(days=1)
    first_of_previous_month = first_of_previous_month.replace(day=1)

    print(f"Эта задача выполняется в 7:00 первого числа предыдущего месяца - {first_of_previous_month.strftime('%B %Y')}")

# Запланируйте выполнение задачи в 7:00 первого числа каждого месяца
schedule.every().month.on(1).at("07:00").do(task_at_start_of_previous_month).tag("start_of_previous_month")

# Главный цикл, который будет проверять и выполнять запланированные задачи
while True:
    schedule.run_pending()
    time.sleep(1)