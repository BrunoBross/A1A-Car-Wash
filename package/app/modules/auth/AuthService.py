from package.app.meta.Singleton import Singleton
from package.app.modules.auth.AuthView import AuthView
from package.app.template.IAppModule import IAppModule

RESPONSE_MAP = {
    'OK': True,
    'NAO OK': False
}

class AuthService(metaclass=Singleton):

    def __init__(self):
        self.__authView = AuthView()

    def getAuthentication(self) -> bool:
        val = self.__authView.login()
        return RESPONSE_MAP[val[0]] 
