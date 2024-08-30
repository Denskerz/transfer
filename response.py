

{
    "model_id": "XXX",
    "tables": [
        {
            "id_table": "XXX",
            "features": ["feature_1", "feature_2"]
        },
        {
            "id_table": "XXX",
            "features": ["feature_1", "feature_2"]
        }
    ],
    "train_csv": "name_csv",
    "tests": "XXX",
    "upload": true,
    "response": true
}


import pymqi

# Параметры подключения к IBM MQ
QUEUE_MANAGER = 'QM_NAME'
CHANNEL = 'CHANNEL_NAME'
HOST = 'HOST_NAME'
PORT = 1414
USER = 'USER_NAME'
PASSWORD = 'PASSWORD'

# Параметры очереди
QUEUE_NAME = 'QUEUE_NAME'

try:
    # Создание контекста подключения к IBM MQ
    qmgr = pymqi.QueueManager(None)
    cd = pymqi.CD()
    cd.ChannelName = CHANNEL
    cd.ConnectionName = f"{HOST}({PORT})"
    cd.UserIdentifier = USER
    cd.Password = PASSWORD
    qmgr.connect_tcp_client(QUEUE_MANAGER, 0, cd)

    # Открытие очереди для чтения
    queue = pymqi.Queue(qmgr, QUEUE_NAME)
    message = queue.get()

    # Обработка полученного сообщения
    json_url = message.decode('utf-8')
    print(f"Получена ссылка на JSON-файл: {json_url}")

    # Закрытие очереди и отключение от IBM MQ
    queue.close()
    qmgr.disconnect()

except pymqi.Error as e:
    print(f"Произошла ошибка: {e}")
