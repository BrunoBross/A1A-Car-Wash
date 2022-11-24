from typing import Optional

from package.app.api.modules.user.UserDtoMapper import UserDtoMapper
from package.app.api.modules.user.UserQuery import UserQuery
from package.app.api.modules.user.dto.UserDto import UserDto
from package.app.meta.Singleton import Singleton


class UserService(metaclass=Singleton):
    def __init__(self):
        self.__query = UserQuery()
        self.__userDtoMapper = UserDtoMapper()

    def getUserByUsername(self, username: str) -> Optional[UserDto]:
        user = self.__query.getUserByUsername(username)
        if user:
            return self.__userDtoMapper.mapUserToDto(user)
        return None

    def createUser(self, userDto: UserDto):
        return self.__query.createUser(self.__userDtoMapper.mapDtoToUser(userDto))

    def updateUser(self, userUpdates: list, user_id: int):
        self.__query.updateUser(userUpdates, user_id)
