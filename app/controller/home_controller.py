from fastapi import APIRouter

home_router = APIRouter(tags=["Home"])


class HomeController:

    @staticmethod
    @home_router.get(path="")
    def home() -> dict:
        return {"msg": "HomeController"}
