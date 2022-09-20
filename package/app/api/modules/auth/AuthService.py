from package.app.api.modules.auth.AuthQuery import AuthQuery
from package.app.meta.Singleton import Singleton


class AuthService(metaclass=Singleton):

    def __init__(self):
        self.__authQuery = AuthQuery()

    def authenticate(self, info) -> bool:
        return self.__authQuery.authenticate(info)
