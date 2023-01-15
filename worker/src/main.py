import asyncio

import aio_pika
from core.config import settings
from core.rabbit import RabbitService
from core.sender import SendgridService
from core.worker import Worker
from sendgrid import SendGridAPIClient

async def main():
    rabbit_connection = await aio_pika.connect_robust(settings.rabbit_dsn)
    rabbit_service = RabbitService(connection=rabbit_connection)
    sender_service = SendgridService(client=SendGridAPIClient(settings.api_key))
    queue_list = settings.all_queues
    workers = []
    for queue in queue_list.split(","):
        worker = Worker(
            rabbit_service=rabbit_service,
            sender_service=sender_service,
            rabbit_task_queue=queue
        )
        workers.append(worker.work())
    await asyncio.gather(*workers)
    await rabbit_connection.close()


if __name__ == "__main__":
    asyncio.run(main())
