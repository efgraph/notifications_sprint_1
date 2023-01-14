from pydantic import BaseModel


class EmailData(BaseModel):
    """Модель сообщения для отправки по email"""

    email: str
    subject: str
    text: str
