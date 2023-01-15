import asyncio
from typing import List

import aio_pika
from config import settings


async def declare_queues(queues: List[str]):
    """Объявляем очереди до старта api"""
    connection: aio_pika.RobustConnection = await aio_pika.connect_robust(url=settings.rabbit_dsn)
    async with connection.channel() as channel:
        for queue in queues:
            await channel.declare_queue(name=queue, durable=True)

    await connection.close()


if __name__ == "__main__":
    queues = settings.all_queues.split(",")
    asyncio.run(declare_queues(queues=queues))
