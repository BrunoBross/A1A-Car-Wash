from typing import Optional
from package.app.api.modules.auth.AuthQuery import AuthQuery
from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.api.modules.user.UserDtoMapper import UserDtoMapper
from package.app.api.modules.user.dto.UserDto import UserDto
from package.app.meta.Singleton import Singleton
from package.app.api.crypt.utils import matchHash


class AuthService(metaclass=Singleton):
    def __init__(self):
        self.__query = AuthQuery()
        self.__userDtoMapper = UserDtoMapper()

    def authenticate(self, data: AuthDto) -> Optional[UserDto]:
        print(data)
        user = self.__query.getUserByUsername(data.username)
        if user:
            if matchHash(data.password, user.password):
                print("success")
                return self.__userDtoMapper.mapUserToDto(user)
        print("failure")
        return None
