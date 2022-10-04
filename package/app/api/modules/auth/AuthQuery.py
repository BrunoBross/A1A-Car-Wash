from typing import Optional
from package.app.api.model.User import User
from package.app.api.orm.DAO import DAO
from package.app.meta.Singleton import Singleton


class AuthQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()

    def getUserByUsername(self, username: str) -> Optional[User]:
        return self.__dao.select(User).where(User.username == username).first()
