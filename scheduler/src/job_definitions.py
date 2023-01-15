import asyncio
import json

import aio_pika
from config import settings
from async_client import get_top5, get_users
from rabbit import publish_top5_event

loop = asyncio.new_event_loop()
rabbit_connection: aio_pika.RobustConnection = loop.run_until_complete(
    aio_pika.connect_robust(url=settings.rabbit_dsn)
)

def saved_films():
    top5 = loop.run_until_complete(get_top5())
    users = loop.run_until_complete(get_users())
    for user in users:
        user["films"] = top5
        loop.run_until_complete(publish_top5_event(rabbit_connection, json.dumps(user)))
