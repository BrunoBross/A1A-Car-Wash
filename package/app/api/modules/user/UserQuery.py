from typing import Optional
from package.app.api.model.User import User
from package.app.api.orm.DAO import DAO
from package.app.meta.Singleton import Singleton
from package.app import sqlalchemy_session


class UserQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()
        self.__session = sqlalchemy_session

    def getUserByUsername(self, username: str) -> Optional[User]:
        return self.__dao.select(User).where(User.username == username).first()

    def createUser(self, user: User):
        return self.__dao.insert(user)

    def updateUser(self, userUpdates: list, user_id: int):
        for update in userUpdates:
            self.__session.query(User).where(User.id == user_id).update(update)

            self.__session.commit()

    def deleteUser(self, user_id: int):
        self.__dao.delete(User).where(User.id == user_id)
