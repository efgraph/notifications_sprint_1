from pydantic.env_settings import BaseSettings
from pydantic.fields import Field
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("worker")


class Settings(BaseSettings):
    rabbit_dsn: str = Field('amqp://guest:guest@rabbit:5672', env='rabbit_dsn')
    from_email: str = Field('vasya@yandex.ru', env='from_email')
    api_key: str = Field("", env='SendgridAPIKEY')
    all_queues: str = Field(
        'administration_event:queue,registration_event:queue,rating_review_event:queue,scheduler_bookmarks_event:queue',
        env='all_queues')


settings = Settings()
