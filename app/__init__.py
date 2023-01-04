from fastapi import FastAPI
from app.controller import ping_router, user_router


def create_app() -> FastAPI:
    app = FastAPI(title="Store API")

    app.include_router(ping_router, prefix="/ping")
    app.include_router(user_router, prefix="/user")

    return app
