from typing import Any, Type

from sqlalchemy.orm import Query

from package.app import sqlalchemy_session, sqlalchemy_base
from package.app.meta.Singleton import Singleton


class DAO(metaclass=Singleton):
    def __init__(self):
        self.__session = sqlalchemy_session

    def query(self, model: Type[sqlalchemy_base]) -> Query:
        return self.__session.query(model)

