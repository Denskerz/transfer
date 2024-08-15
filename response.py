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


podman run -d \
  -v //172.30.56.144/share:/mnt/share:guest,cifs,username=eroshevich_d,password=112q34e56t,domain=sigma-belpsb.by \
  your-image

docker run -v //172.30.56.144/share:/mnt/share:cifs -e CIFS_USERNAME=eroshevich_d -e CIFS_PASSWORD=112q34e56t -e CIFS_DOMAIN=sigma-belpsb.by your-image
