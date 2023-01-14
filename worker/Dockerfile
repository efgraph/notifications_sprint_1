FROM python:3.9-slim
EXPOSE 12345
WORKDIR /worker

RUN apt-get update && apt-get --yes upgrade

COPY requirements.txt requirements.txt
RUN  pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY . .

WORKDIR ./src

CMD python core/waiter.py && python main.py

