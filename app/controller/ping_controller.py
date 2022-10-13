from fastapi import APIRouter

ping_router = APIRouter(tags=["Ping"])


class PingController:

    @staticmethod
    @ping_router.get(path="")
    def pong() -> str:
        return "pong"
