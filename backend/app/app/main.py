from fastapi import FastAPI
from pydantic import BaseModel

from app.core.config import settings

app = FastAPI(
    debug=settings.DEBUG,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


class Index(BaseModel):
    message: str


@app.get("/", response_model=Index)
def index():
    return {"message": "Hello world!"}
