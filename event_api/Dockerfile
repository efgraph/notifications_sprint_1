FROM python:3.9-slim

WORKDIR /event_api

RUN apt-get update && apt-get --yes upgrade

COPY requirements.txt requirements.txt
RUN  pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY . .

RUN chmod +x /event_api/docker-entrypoint.sh

ENTRYPOINT sh /event_api/docker-entrypoint.sh

EXPOSE 10000