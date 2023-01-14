FROM python:3.9-slim-buster

WORKDIR /scheduler

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN  pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY . .

WORKDIR ./src

CMD python waiter.py && gunicorn main:app -b 0.0.0.0:4400 --reload