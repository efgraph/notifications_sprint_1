import http
import requests
from settings.config import settings


def test_registration_notification():
    response = requests.post(f"{settings.api_url}{settings.api_registration_path}", json={
        "firstname": "Petr",
        "subject": "Message Subject",
        "text": "Hello ...",
        "email": "petr@yandex.ru"
    })
    assert response.status_code == http.HTTPStatus.OK
