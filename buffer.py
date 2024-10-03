#!/usr/bin/expect

set timeout -1

# Ваша команда
spawn your_command

# Ожидание запроса пароля
expect "Password:"
send "your_password\r"

# Ожидание завершения команды
expect eof