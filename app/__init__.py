from fastapi import FastAPI
from app.controller import home_router, ping_router


def create_app() -> FastAPI:
    app = FastAPI(title="Store API")

    app.include_router(home_router, prefix="/home")
    app.include_router(ping_router, prefix="/ping")

    return app
