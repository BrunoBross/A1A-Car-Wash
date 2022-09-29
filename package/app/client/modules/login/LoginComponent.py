from package.app.api.modules.auth.AuthController import AuthController
from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.client.gui.window.WindowService import WindowService
from package.app.client.state.UserContext import UserContext
from package.app.meta.Singleton import Singleton


class LoginComponent(metaclass=Singleton):
    def __init__(self):
        self.__authController = AuthController()
        self.__userContext = UserContext()

    def requestAuth(self, username: str, password: str):
        return self.__authController.authenticate(AuthDto(username, password))
