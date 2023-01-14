FROM python:3.9-slim

WORKDIR /event_api

RUN apt-get update && apt-get --yes upgrade

COPY requirements.txt requirements.txt
RUN  pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY . .

WORKDIR ./src
CMD python core/waiter.py && python core/up_rabbit_queues.py && uvicorn main:app --host 0.0.0.0 --port 10000 --reload

EXPOSE 10000