from typing import Callable, Dict, Set
from package.app.client.modules.login.LoginEventEnum import LoginEventEnum as EventEnum
from package.app.meta.Singleton import Singleton


class LoginEventManager(metaclass=Singleton):
    def __init__(self):
        self.__subscribers: Dict[EventEnum, Set[Callable]] = {
            EventEnum.STARTUP: set(),
            EventEnum.LOGIN: set(),
            EventEnum.LOGOUT: set(),
        }

    def subscribe(self, event: EventEnum, callback: Callable):
        self.__subscribers[event].add(callback)

    def unsubscribe(self, event: EventEnum, callback: Callable):
        self.__subscribers[event].remove(callback)

    def post(self, event: EventEnum, *args, **kwargs):
        for fn in self.__subscribers[event]:
            fn(*args, **kwargs)
