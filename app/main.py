from fastapi import FastAPI

from .config import Settings
from .schemas import SimpleSchema
from .routers import simple_route

settings = Settings()

app = FastAPI(title=settings.title)
app.include_router(simple_route)


@app.get("/", response_model=SimpleSchema)
async def root():
    return SimpleSchema(message="Hello, World!")
