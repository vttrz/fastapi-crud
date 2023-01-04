from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session
from typing import List
from app.repository import UserRepository
from app.model.domain import UserDomain
from app.model.response import UserResponse
from app.model.request import UserRequest, UpdateNameRequest


class UserService:

    def list(self, db: Session) -> List[UserResponse]:
        users: List[UserDomain] = UserRepository.list(db=db)

        users_response: List[UserResponse] = list(map(lambda u: self.__parse_user_domain_to_user_response(user=u),
                                                      users))

        return users_response

    def get(self, user_id: int, db: Session) -> UserResponse:
        user: UserDomain = UserRepository.get(user_id=user_id, db=db)

        if not user:
            raise HTTPException(detail="User not found", status_code=HTTP_404_NOT_FOUND)

        return self.__parse_user_domain_to_user_response(user=user)

    def create(self, user_request: UserRequest, db: Session):

        user_entity: UserDomain = UserDomain(name=user_request.name,
                                             email=user_request.email,
                                             password=user_request.password)

        user: UserDomain = UserRepository.create(user=user_entity, db=db)

        return self.__parse_user_domain_to_user_response(user=user)

    def update(self, user_id: int, user_update: UpdateNameRequest, db: Session) -> None:

        user_entity: UserDomain = UserDomain(id=user_id, name=user_update.name)

        user: UserDomain = UserRepository.update(user=user_entity, db=db)

        return

    @staticmethod
    def delete(user_id: int, db: Session) -> None:
        UserRepository.delete(user_id=user_id, db=db)
        return

    @staticmethod
    def __parse_user_domain_to_user_response(user: UserDomain) -> UserResponse:
        return UserResponse(id=user.id, name=user.name, email=user.email)
