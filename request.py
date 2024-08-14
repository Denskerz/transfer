FROM 172.30.71.8:5001/images/ubi9-python311:latest

USER root


COPY ./pip.conf /etc/pip.conf
COPY . .

RUN microdnf install -y cifs-utils
RUN pip3 install -r ./requirements.txt
