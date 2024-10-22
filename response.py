import logging

# Настройка конфигурации логирования
logging.basicConfig(
    level=logging.DEBUG,  # Уровень важности (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат сообщения
    filename='app.log',  # Файл для записи логов
    filemode='w'  # Режим записи (w - перезапись, a - добавление)
)

# Примеры логирования
logging.debug('Это сообщение отладки')
logging.info('Это информационное сообщение')
logging.warning('Это предупреждение')
logging.error('Это сообщение об ошибке')
logging.critical('Это критическая ошибка')