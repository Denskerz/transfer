FROM 172.30.71.8:5001/images/ubi9-python311:latest

USER root

COPY ./pip.conf /etc/pip.conf
COPY . .

# Копируем и устанавливаем недостающие зависимости
COPY keyutils-1.6.1-3.el9.x86_64.rpm /tmp/
COPY libwbclient-4.15.5-9.el9.x86_64.rpm /tmp/
RUN rpm -i /tmp/keyutils-1.6.1-3.el9.x86_64.rpm
RUN rpm -i /tmp/libwbclient-4.15.5-9.el9.x86_64.rpm

# Копируем и устанавливаем cifs-utils
COPY cifs-utils-7.0-5.el9.x86_64.rpm /tmp/
RUN rpm -i /tmp/cifs-utils-7.0-5.el9.x86_64.rpm

# Копируем файл с CIFS-конфигурацией и монтируем ресурс
COPY cifs_mount.txt /etc/
RUN mkdir /mnt && mount -a

RUN pip3 install -r ./requirements.txt