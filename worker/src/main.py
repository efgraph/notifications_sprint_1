import asyncio
import os

import aio_pika
from core.rabbit import RabbitService
from core.sender import SendgridService
from core.worker import Worker
from sendgrid import SendGridAPIClient


async def main():
    rabbit_connection = await aio_pika.connect_robust(
        url=os.getenv("RABBIT_DSN", "amqp://guest:guest@rabbit:5672/")
    )
    rabbit_service = RabbitService(connection=rabbit_connection)
    sender_service = SendgridService(
        client=SendGridAPIClient(api_key=os.getenv("SendgridAPIKEY", ""))
    )
    queue_list = os.getenv(
        "ALL_QUEUES",
        "administration_event:queue,registration_event:queue,rating_review_event:queue,scheduler_bookmarks_event:queue",
    )
    workers = []
    for queue in queue_list.split(","):
        worker = Worker(
            rabbit_service=rabbit_service,
            sender_service=sender_service,
            rabbit_task_queue=queue,
        )
        workers.append(worker.work())
    await asyncio.gather(*workers)
    await rabbit_connection.close()


if __name__ == "__main__":
    asyncio.run(main())
