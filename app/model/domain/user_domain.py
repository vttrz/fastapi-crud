from sqlalchemy import DateTime, Column, Integer, String
from datetime import datetime

from app.config import Base


class UserDomain(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    createdAt = Column(DateTime, default=datetime.utcnow())
    updatedAt = Column(DateTime, onupdate=datetime.utcnow(), nullable=True, default=None)
