import asyncio
import os

import aio_pika


async def waiter_rabbit():
    """Waiter для rabbitmq"""
    rabbit_status = 0
    while not rabbit_status:
        try:
            connection = await aio_pika.connect_robust(
                url=os.getenv("RABBIT_DSN", "amqp://guest:guest@rabbit:5672/")
            )
            await connection.close()
            rabbit_status = 1
        except ConnectionError:
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(waiter_rabbit())
