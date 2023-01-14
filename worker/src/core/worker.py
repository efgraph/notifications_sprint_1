import asyncio
import os

from core.rabbit import RabbitService
from core.sender import SendgridService
from models import models
from pydantic import ValidationError


class Worker:
    """Класс Worker"""

    def __init__(
        self,
        rabbit_service: RabbitService,
        sender_service: SendgridService,
        rabbit_task_queue: str,
    ):
        """"""
        self.rabbit = rabbit_service
        self.sender = sender_service
        self.task_queue = rabbit_task_queue

    async def handling_message(self, message):
        """Метод в обработки сообщений"""
        message_to_send = await self.prepare_message_to_send(message=message)
        if message_to_send:
            await self.sender.send(message=message_to_send)


    async def prepare_message_to_send(self, message):
        """Метод подготовки сообщения для отправки"""
        try:
            message_to_send = ""
            if self.task_queue == os.getenv(
                "REGISTRATION_EVENT_QUEUE", "registration_event:queue"
            ):
                message = models.RegistrationEmailModel(
                    firstname=message.get("firstname"), email=message.get("email")
                )
                message_to_send = models.EmailData(
                    email=message.email,
                    subject=message.subject,
                    text=f"Hello, thank you for registering",
                )
            elif self.task_queue == os.getenv(
                "ADMINISTRATION_EVENT_QUEUE", "administration_event:queue"
            ):
                message = models.EmailData(
                    email=message["email"],
                    subject=message["subject"],
                    text=message["text"],
                )
                message_to_send = models.EmailData(
                    email=message.email, subject=message.subject, text=message.text
                )
            elif self.task_queue == os.getenv(
                "SCHEDULER_BOOKMARKS_Q", "scheduler_bookmarks_event:queue"
            ):
                message_to_send = models.EmailData(
                    email=message["email"],
                    subject="Top Movies",
                    text=", ".join(message["films"]),
                )
            return message_to_send
        except ValidationError as err:
            print(err)

    async def work(self):
        """Метод собирает асинхронные задачи и запускает их"""
        tasks = []
        while message := await self.rabbit.consume_from_queue(queue=self.task_queue):
            tasks.append(asyncio.create_task(self.handling_message(message=message)))
        await asyncio.gather(*tasks)
