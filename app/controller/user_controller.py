from fastapi import APIRouter, Depends
from starlette.status import HTTP_204_NO_CONTENT
from typing import List
from sqlalchemy.orm import Session
from app.config import get_db
from app.service import UserService
from app.model.response import UserResponse
from app.model.request import UserRequest, UpdateNameRequest

# Only doing this because i'm not using any lib of database migration -> Ex: alembic
from app.model.domain.user_domain import Base
from app.config import engine

Base.metadata.create_all(bind=engine)
# -------

user_router = APIRouter(tags=["User"])


class UserController:

    @staticmethod
    @user_router.get(path="/all", response_model=List[UserResponse])
    def list(db: Session = Depends(get_db)):
        return UserService.list(db=db)

    @staticmethod
    @user_router.get(path="/{user_id}", response_model=UserResponse)
    def get(user_id: int, db: Session = Depends(get_db)):
        return UserService.get(user_id=user_id, db=db)

    @staticmethod
    @user_router.post(path="", response_model=UserResponse)
    def store(user: UserRequest, db: Session = Depends(get_db)):
        return UserService.create(user_request=user, db=db)

    @staticmethod
    @user_router.put(path="/{user_id}", status_code=HTTP_204_NO_CONTENT)
    def edit(user_id: int, user: UpdateNameRequest, db: Session = Depends(get_db)):
        return UserService.update(user_id=user_id, user_update=user, db=db)

    @staticmethod
    @user_router.delete(path="/{user_id}")
    def delete(user_id: int, db: Session = Depends(get_db)):
        return UserService.delete(user_id=user_id, db=db)
