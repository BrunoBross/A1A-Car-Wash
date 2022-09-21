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
        return self.__userDtoMapper.mapUserToDto(self.__query.getUserByUsername(username))

