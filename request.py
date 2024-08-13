import requests
import json
from datetime import datetime, timedelta

# Получаем текущую дату и предыдущую дату
current_date = datetime.now().date()
previous_date = current_date - timedelta(days=1)

# Формируем тело запроса в формате JSON
request_body = {
    "start_date": str(previous_date),
    "end_date": str(current_date)
}

# Отправляем POST-запрос с телом запроса
response = requests.post("http://0.0.0.0:8040/start", data=json.dumps(request_body), headers={"Content-Type": "application/json"})

# Проверяем статус ответа
if response.status_code == 200:
    print("Запрос успешно отправлен")
else:
    print(f"Ошибка при отправке запроса: {response.status_code} - {response.text}")
