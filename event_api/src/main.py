
import aio_pika
import uvicorn as uvicorn
from api.v1 import event
from core import config, rabbit
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI(
    title=config.PROJECT_NAME,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


@app.on_event("startup")
async def startup():
    rabbit.rabbit_connection = await aio_pika.connect_robust(url=config.RABBIT_DSN)


@app.on_event("shutdown")
async def shutdown():
    await rabbit.rabbit_connection.close()


app.include_router(event.router, prefix='/api/v1/event')

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=10000,
        reload=True,
    )
