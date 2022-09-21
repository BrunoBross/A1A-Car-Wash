from package.app.api.modules.auth.AuthQuery import AuthQuery
from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.api.modules.user.UserService import UserService
from package.app.meta.Singleton import Singleton
from package.app.api.crypt.utils import matchHash


class AuthService(metaclass=Singleton):

    def __init__(self):
        self.__query = AuthQuery()
        self.__userService = UserService()

    def authenticate(self, data: AuthDto) -> bool:
        user = self.__userService.getUserByUsername(data.username)
        if not user: return False
        return matchHash(data.password, user.passwordHash)
