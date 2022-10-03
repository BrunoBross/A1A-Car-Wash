from package.app.api.modules.auth.AuthController import AuthController
from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.client.event.EventEnum import EventEnum
from package.app.client.event.EventManager import EventData, EventManager
from package.app.client.state.UserContext import UserContext
from package.app.meta.Singleton import Singleton


class LoginComponent(metaclass=Singleton):
    def __init__(self):
        self.__authController = AuthController()
        self.__userContext = UserContext()
        self.__eventManager = EventManager()

    def requestAuth(self, username: str, password: str):
        userData = self.__authController.authenticate(AuthDto(username, password))
        if userData:
            self.__eventManager.post(EventEnum.LOGIN, userData)
