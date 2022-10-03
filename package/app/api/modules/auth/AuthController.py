from typing import Optional
from package.app.api.modules.auth.AuthService import AuthService
from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.api.modules.user.dto.UserDto import UserDto
from package.app.meta.Singleton import Singleton


class AuthController(metaclass=Singleton):
    def __init__(self):
        self.__authService = AuthService()

    def authenticate(self, data: AuthDto) -> Optional[UserDto]:
        return self.__authService.authenticate(data)
