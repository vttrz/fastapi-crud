from typing import List, Optional
from sqlalchemy.orm import Session
from app.model.domain import UserDomain


class UserRepository:

    @staticmethod
    def list(db: Session) -> List[UserDomain]:
        return db.query(UserDomain).all()

    @staticmethod
    def get(user_id: int, db: Session) -> Optional[UserDomain]:
        return db.query(UserDomain).filter(UserDomain.id == user_id).one_or_none()

    @staticmethod
    def create(user: UserDomain, db: Session) -> UserDomain:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def update(user: UserDomain, db: Session) -> UserDomain:
        user = db.query(UserDomain).filter(UserDomain.id == user.id).update({UserDomain.name: user.name})
        db.commit()
        return user

    @staticmethod
    def delete(user_id: int, db: Session) -> None:
        db.query(UserDomain).filter(UserDomain.id == user_id).delete()
        db.commit()
