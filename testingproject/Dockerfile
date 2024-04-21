FROM python:3.12

RUN mkdir testingproject
WORKDIR testingproject

ADD requirements.txt /testingproject/
RUN pip install -r requirements.txt
ADD . /testingproject/

ADD .docker.env /testingproject/.env
ENV APP_NAME=DOCKER_DEMO

RUN pip3 install -r requirements.txt


CMD gunicorn docker_demo.wsgi:application -b 127.0.0.1:8000