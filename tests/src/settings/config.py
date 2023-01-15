from pydantic.env_settings import BaseSettings
from pydantic.fields import Field


class Settings(BaseSettings):
    api_url: str = Field('http://api:10000', env='api_url')
    api_ping_path: str = Field('/api/v1/event/ping', env='api_ping_path')
    api_registration_path: str = Field('/api/v1/event/administrator_message', env='api_registration_path')


settings = Settings()
