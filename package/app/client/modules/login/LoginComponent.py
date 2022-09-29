from package.app.api.modules.auth.AuthController import AuthController
from package.app.meta.Singleton import Singleton


class LoginComponent(metaclass=Singleton):
    def __init__(self):
        self.__authController = AuthController()
