FROM python:3.10

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE 'config.settings'

COPY requirements.txt requirements.txt

RUN apt update && apt -y upgrade && apt install -y netcat postgresql-client\
 python3-setuptools && pip install pipenv

RUN  mkdir -p /opt/app/static/ \
     && pip install --upgrade pip \
     && pip install -r requirements.txt

COPY . .

RUN chmod +x /opt/app/docker-entrypoint.sh

ENTRYPOINT sh /opt/app/docker-entrypoint.sh

EXPOSE 8000