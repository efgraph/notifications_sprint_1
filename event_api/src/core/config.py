from pydantic import BaseSettings
from pydantic.fields import Field


class Settings(BaseSettings):
    rabbit_dsn: str = Field('amqp://guest:guest@rabbit:5672', env='rabbit_dsn')
    event_routing_key_admin: str = Field("administration_event:queue", env='administration_event_queue')
    event_registration_key: str = Field('registration_event:queue', env='registration_event_queue')
    all_queues: str = Field('administration_event:queue,registration_event:queue,'
                            + 'rating_review_event:queue,scheduler_bookmarks_event:queue', env='all_queues')


settings = Settings()
