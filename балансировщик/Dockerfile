FROM 10.244.226.233:5001/images/ubi8-python38-vim:latest

USER root
WORKDIR /opt/server
COPY . .
COPY pip.conf /etc/pip.conf

RUN pip3 install -r requirements.txt

EXPOSE 80
CMD python3 -m uvicorn --host 0.0.0.0 --port 80 server:app
