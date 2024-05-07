from sqlalchemy import Column, Integer

from database import Database


class BaseModel(Database().BASE):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
