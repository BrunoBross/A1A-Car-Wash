from package.app.api.modules.auth.AuthController import AuthController
from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.client.event.EventEnum import EventEnum
from package.app.client.event.EventManager import EventManager
from package.app.client.state.ComponentState import ComponentState
from package.app.client.gui.imports import Gtk
from package.app.client.utils.form import getEntryBuffer
from package.app.meta.Singleton import Singleton


class LoginComponent(metaclass=Singleton):
    def __init__(self):
        self.__authController = AuthController()
        self.__eventManager = EventManager()
        self.__state = ComponentState()

    def requestAuth(self):
        username = getEntryBuffer(self.__state.getReferenceById("username"))
        password = getEntryBuffer(self.__state.getReferenceById("password"))

        userData = self.__authController.authenticate(AuthDto(username, password))
        if userData:
            self.__eventManager.post(EventEnum.LOGIN, userData)
            self.__state.reset()

    def getState(self) -> ComponentState:
        return self.__state
