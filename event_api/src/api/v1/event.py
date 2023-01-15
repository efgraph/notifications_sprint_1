import json
from aio_pika import RobustConnection, Message, DeliveryMode
from core.rabbit import get_rabbit_connection
from core.config import settings
from fastapi import Depends, APIRouter
from models.administration_event import AdministrationEventModel
from models.registration_user_event import RegistrationUserEventModel

router = APIRouter()


@router.get("/ping", tags=["ping"])
async def ping():
    return "ok"


@router.post("/administrator_message/", tags=["events"])
async def add_administration_event(
        administration_event: AdministrationEventModel,
        rabbit_connection: RobustConnection = Depends(get_rabbit_connection),
):
    """Событие от администраторов"""
    async with rabbit_connection.channel() as channel:
        message = Message(
            body=json.dumps(administration_event.dict(), default=str).encode("utf-8"),
            delivery_mode=DeliveryMode.PERSISTENT,
        )
        await channel.default_exchange.publish(
            message,
            routing_key=settings.event_routing_key_admin,
        )


@router.post("/registration/", tags=["events"])
async def add_registration_user_event(
        registration_event: RegistrationUserEventModel,
        rabbit_connection: RobustConnection = Depends(get_rabbit_connection),
):
    """Событие о регистрации пользователя"""
    async with rabbit_connection.channel() as channel:
        message = Message(
            body=json.dumps(registration_event.dict(), default=str).encode("utf-8"),
            delivery_mode=DeliveryMode.PERSISTENT,
        )
        await channel.default_exchange.publish(
            message,
            routing_key=settings.event_registration_key,
        )
