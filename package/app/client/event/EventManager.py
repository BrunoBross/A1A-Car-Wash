from dataclasses import dataclass
from typing import Any, Callable, Dict, Optional, Set
from package.app.client.event.EventEnum import EventEnum
from package.app.meta.Singleton import Singleton


@dataclass
class EventData:
    data: Optional[Any]


EventHandler = Callable[[EventData], Optional[Any]]


class EventManager(metaclass=Singleton):
    def __init__(self):
        self.__subscribers: Dict[EventEnum, Set[EventHandler]] = {
            EventEnum.STARTUP: set(),
            EventEnum.LOGIN: set(),
            EventEnum.LOGOUT: set(),
        }

    def subscribe(self, event: EventEnum, callback: EventHandler):
        self.__subscribers[event].add(callback)

    def unsubscribe(self, event: EventEnum, callback: EventHandler):
        self.__subscribers[event].remove(callback)

    def post(self, event: EventEnum, data: EventData = EventData(data=None)):
        for fn in self.__subscribers[event]:
            fn(data)
