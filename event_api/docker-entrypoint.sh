#!/bin/sh

cd src
python core/waiter.py
python core/up_rabbit_queues.py
uvicorn main:app --host 0.0.0.0 --port 10000 --reload


