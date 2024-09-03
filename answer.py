#!/bin/bash

# Находим PID процессов, которые используют указанную команду
pids=$(pgrep -f "/usr/jdk64/jdk1.8.0_112/bin/java -cp dhsjs")

# Проверяем, найдены ли процессы
if [ -z "$pids" ]; then
    echo "Процессы не найдены."
else
    # Убиваем найденные процессы
    echo "Убиваем процессы с PID: $pids"
    kill $pids
fi