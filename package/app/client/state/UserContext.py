from package.app.client.modules.login.LoginEventEnum import LoginEventEnum
from package.app.client.modules.login.LoginEventManager import LoginEventManager
from package.app.meta.Singleton import Singleton


class UserContext(metaclass=Singleton):
    def __init__(self):
        self.__eventManager = LoginEventManager()
        self.__eventManager.subscribe(LoginEventEnum.LOGIN, self.__setUserContext)
        self.__eventManager.subscribe(LoginEventEnum.LOGOUT, self.__unsetUserContext)

    def isAuthenticated(self) -> bool:
        pass

    def __setUserContext(self):
        print("Setting user context ...")

    def __unsetUserContext(self):
        print("Unsetting user context ...")
