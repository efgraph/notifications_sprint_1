
from os import getenv

import httpx
import orjson

ugc_url = getenv("UGC_URL", "http://fake-server:4000")
bookmark_api_prefix = getenv("TOP_10_API_PREFIX", "/top5/")
ugc_timeout = float(getenv("UGC_TIMEOUT", 60.0))

auth_url = getenv("AUTH_URL", "http://fake-server:4000")
users_api_prefix = getenv("USERS_API_PREFIX", "/users/")


async def get_top5():
    async with httpx.AsyncClient(timeout=ugc_timeout) as client:
        response = await client.get(
            f"{ugc_url}{bookmark_api_prefix}/",
            timeout=httpx.Timeout(timeout=ugc_timeout),
        )
        content = orjson.loads(response.content)
    return content

async def get_users():
    async with httpx.AsyncClient() as client:
        url = f"{auth_url}{users_api_prefix}"
        response = await client.get(url)
    return orjson.loads(response.content)

