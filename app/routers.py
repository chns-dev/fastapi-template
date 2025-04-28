from fastapi import APIRouter

from .services import add
from .schemas import SimpleSchema

simple_route = APIRouter()


@simple_route.get("/ping", response_model=SimpleSchema)
async def ping_pong():
    return SimpleSchema(message="pong")


@simple_route.get("/add", response_model=SimpleSchema)
async def add_numbers(x: int, y: int):
    return SimpleSchema(message=add(x, y))
