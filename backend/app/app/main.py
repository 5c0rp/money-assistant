from fastapi import FastAPI

from app.core.config import settings
from app.api.api_v1.api import api_router


app = FastAPI(
    debug=settings.DEBUG,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    title='Money Assistant',
)

app.include_router(api_router, prefix=settings.API_V1_STR)
