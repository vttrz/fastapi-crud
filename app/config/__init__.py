from app.config.db import DbConfig

Base = DbConfig.Base
get_db = DbConfig().get_db
engine = DbConfig.engine

__all__ = ["Base", "get_db", "engine"]
