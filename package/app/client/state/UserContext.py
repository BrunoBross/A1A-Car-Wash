from typing import Optional
from package.app.api.enum.RoleEnum import RoleEnum
from package.app.api.modules.user.dto.UserDto import UserDto
from package.app.client.event.EventEnum import EventEnum
from package.app.client.event.EventManager import EventData, EventManager
from package.app.meta.Singleton import Singleton


class UserContext(metaclass=Singleton):
    def __init__(self):
        self.__data: Optional[UserDto]
        self.__eventManager = EventManager()
        self.__subscribeSetup()

    def isAuthenticated(self) -> bool:
        return bool(self.__data)

    def get(self) -> Optional[UserDto]:
        return self.__data

    def __setUserContext(self, data: EventData):
        self.__data = data.data
        print("Setting user context ...")

    def __unsetUserContext(self, _: EventData):
        self.__data = None
        print("Unsetting user context ...")

    def __subscribeSetup(self):
        self.__eventManager.subscribe(EventEnum.LOGIN, self.__setUserContext)
        self.__eventManager.subscribe(EventEnum.LOGOUT, self.__unsetUserContext)
