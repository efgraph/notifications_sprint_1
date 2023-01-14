import os

PROJECT_NAME = "event_api"
RABBIT_DSN = os.getenv("RABBIT_DSN", "amqp://guest:guest@localhost:5672/")
