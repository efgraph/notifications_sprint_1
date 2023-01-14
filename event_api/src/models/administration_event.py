from pydantic import EmailStr, BaseModel


class AdministrationEventModel(BaseModel):
    """Модель данных события от администратора."""

    firstname: str
    subject: str
    text: str
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "firstname": "Petr",
                "subject": "Message Subject",
                "text": "Hello ...",
                "email": "petr@yandex.ru",
            }
        }
