import http
import requests
from requests.exceptions import ConnectionError
import backoff
from settings.config import settings


class ApiCheck:

    @backoff.on_predicate(backoff.fibo, max_value=10)
    @backoff.on_exception(backoff.expo, ConnectionError)
    def ping(self) -> bool:
        response = requests.get(f"{settings.api_url}{settings.api_ping_path}")
        if response.status_code == http.HTTPStatus.OK:
            print('ok')
            return True
        return False


ApiCheck().ping()
