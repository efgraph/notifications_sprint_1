FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'config.settings'

RUN mkdir /app
WORKDIR /app/

COPY requirements.txt requirements.txt

RUN apt update && apt -y upgrade && apt install -y netcat postgresql-client\
 python3-setuptools && pip install pipenv

RUN  mkdir -p /app/static/ \
     && pip install --upgrade pip \
     && pip install -r requirements.txt

COPY . .

RUN chmod +x /app/docker-entrypoint.sh

ENTRYPOINT sh /app/docker-entrypoint.sh

EXPOSE 8000