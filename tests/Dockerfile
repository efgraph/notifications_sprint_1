FROM python:3.9-slim-buster

ENV PYTHONPATH="${PYTHONPATH}:/opt/tests/src/"

WORKDIR /opt/tests

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip \
     && pip install --no-cache-dir -r requirements.txt

COPY . .


