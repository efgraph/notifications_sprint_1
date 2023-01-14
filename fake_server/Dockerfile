FROM node:lts-bullseye-slim

WORKDIR /json-server

RUN npm install -g json-server

COPY . .

CMD json-server --watch ./db.json --port 4000 --host 0.0.0.0

EXPOSE 4000