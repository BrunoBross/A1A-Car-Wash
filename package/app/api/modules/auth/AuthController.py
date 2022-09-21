from package.app.api.modules.auth.AuthService import AuthService
from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.meta.Singleton import Singleton


class AuthController(metaclass=Singleton):

    def __init__(self):
        self.__authService = AuthService()

    def authenticate(self, data: AuthDto) -> bool:
        return self.__authService.authenticate(data)
