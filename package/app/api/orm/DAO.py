from typing import Type
from sqlalchemy.orm import Query
from package.app import sqlalchemy_session, sqlalchemy_base
from package.app.decorators import safe_query
from package.app.meta.Singleton import Singleton


class DAO(metaclass=Singleton):
    def __init__(self):
        self.__session = sqlalchemy_session

    @safe_query
    def select(self, model: Type[sqlalchemy_base]) -> Query:
        return self.__session.query(model)

    @safe_query
    def insert(self, model: Type[sqlalchemy_base]) -> None:
        self.__session.add(model)
        self.__session.commit()

    @safe_query
    def delete(self, model: Type[sqlalchemy_base]) -> None:
        self.__session.delete(model)
        self.__session.commit()

    @safe_query
    def update(self, model: Type[sqlalchemy_base], filter_condition, field, value) -> None:
        self.__session.query(model).filter(filter_condition).update({field:value})
        self.__session.commit()
        
