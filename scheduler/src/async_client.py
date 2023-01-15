import httpx
import orjson

from config import settings


async def get_top5():
    async with httpx.AsyncClient(timeout=settings.ugc_timeout) as client:
        response = await client.get(
            f"{settings.ugc_url}{settings.bookmark_api_prefix}/",
            timeout=httpx.Timeout(timeout=settings.ugc_timeout),
        )
        content = orjson.loads(response.content)
    return content


async def get_users():
    async with httpx.AsyncClient() as client:
        url = f"{settings.auth_url}{settings.users_api_prefix}"
        response = await client.get(url)
    return orjson.loads(response.content)
