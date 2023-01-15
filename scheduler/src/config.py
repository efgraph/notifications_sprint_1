from pydantic import BaseSettings
from pydantic.fields import Field


class Settings(BaseSettings):
    rabbit_dsn: str = Field('amqp://guest:guest@rabbit:5672', env='rabbit_dsn')
    postgres_dsn: str = Field('postgresql://postgres:password@db:5432', env='postgres_dsn')

    ugc_url: str = Field('http://fake-server:4000', env='ugc_url')
    bookmark_api_prefix: str = Field('/top5/', env='top_10_api_prefix')
    ugc_timeout: float = Field(60.0, env='ugc_timeout')

    auth_url: str = Field('http://fake-server:4000', env='auth_url')
    users_api_prefix: str = Field('/users/', env='users_api_prefix')


settings = Settings()
