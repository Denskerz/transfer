import pymqi
import json
import pandas as pd

# Параметры подключения
HOST = 'mb-gw3psifs.belpsb.by'
PORT = 1414
CHANNEL = 'BZI.SVRCONN'
QUEUE_MANAGER = 'MBY.ESB.AC0.GW3'
QUEUE_NAME = 'ESB.BZI.REQUEST'
USER = 'bziusr'
PASSWORD = 'your_password_here'

# Создание контекста соединения
qmgr = pymqi.QueueManager(None)
cd = pymqi.CD()
cd.ChannelName = CHANNEL
cd.ConnectionName = f'{HOST}({PORT})'
cd.UserIdentifier = USER
cd.Password = PASSWORD
qmgr.connect_with_options(QUEUE_MANAGER, cd)

# Создание очереди
queue = pymqi.Queue(qmgr, QUEUE_NAME)

# Получение сообщения
message = queue.get()

# Разбор полученного сообщения
data = json.loads(message)
url = data['url']

# Получение датафрейма из JSON-файла
df = pd.read_json(url)

# Закрытие соединения
queue.close()
qmgr.disconnect()

# Работа с полученным датафреймом
print(df)


есть некоторые данные, которые могут помочь для подключения к очереди IBM-MQ:

AdapterCURS; 20240813_1250
AppDirectoryData; 20240813_1433
AdapterBZI.20240603_1245
для ПСИ\ПРОМа в домене BELPSB зарегистрирован пользователь bziusr и группа bzimqi
пользователь bziusr добавлен в группу mqmmqi и bzimqi.
параметры подключения к КСШ на ПСИ для АС "База залогового имущества" :
хост: mb-gw3psifs.belpsb.by
порт 1414
менеджер: MBY.ESB.AC0.GW3
канал BZI.SVRCONN
шифрование TLS_RSA_WITH_AES_128_CBC_SHA256
SSL ключи те же что и для ИФТ контура
Очередь для получения нотификаций (в том числе sendDirectoryDataNf): ESB.BZI.REQUEST

суть задачи:
необходимо написать подключение к очереди ibm-mq на python, мой сервис будет ждать сообщение, которое мне отправят, в сообщении будет ссылка на json файл, из которого необходимо будет забрать датафрейм 
