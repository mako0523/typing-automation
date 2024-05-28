FROM python:3.12.3-alpine3.20

WORKDIR /home
COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
