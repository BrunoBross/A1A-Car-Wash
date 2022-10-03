from typing import Optional
from package.app.api.modules.user.dto.UserDto import UserDto
from package.app.client.event.EventEnum import EventEnum
from package.app.client.event.EventManager import EventData, EventManager
from package.app.meta.Singleton import Singleton


def getEmptyUser():
    return UserDto(None, None, None)


class UserContext(metaclass=Singleton):
    def __init__(self):
        self.__data: UserDto = getEmptyUser()
        self.__eventManager = EventManager()
        self.__subscribeSetup()

    def isAuthenticated(self) -> bool:
        return bool(self.__data.role)

    def get(self) -> Optional[UserDto]:
        return self.__data

    def __setUserContext(self, data: EventData):
        if isinstance(data.data, UserDto):
            self.__data = data.data
            self.__eventManager.post(EventEnum.CONTEXT_SET)

    def __unsetUserContext(self, _: EventData):
        self.__data = getEmptyUser()

    def __subscribeSetup(self):
        self.__eventManager.subscribe(EventEnum.LOGIN, self.__setUserContext)
        self.__eventManager.subscribe(EventEnum.LOGOUT, self.__unsetUserContext)
