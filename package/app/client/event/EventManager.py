from dataclasses import dataclass
from typing import Any, Callable, Dict, Optional, Set
from package.app.client.event.EventEnum import EventEnum
from package.app.meta.Singleton import Singleton


@dataclass
class EventData:
    data: Optional[Any]


EventHandlerCallback = Callable[[EventData], Optional[Any]]


class EventManager(metaclass=Singleton):
    def __init__(self):
        self.__subscribers: Dict[EventEnum, Set[EventHandlerCallback]] = {
            EventEnum.STARTUP: set(),
            EventEnum.LOGIN: set(),
            EventEnum.LOGOUT: set(),
            EventEnum.CONTEXT_SET: set(),
        }

    def subscribe(self, event: EventEnum, callback: EventHandlerCallback):
        self.__subscribers[event].add(callback)

    def unsubscribe(self, event: EventEnum, callback: EventHandlerCallback):
        self.__subscribers[event].remove(callback)

    def post(self, event: EventEnum, data: Optional[Any] = None):
        eventData = EventData(data=data)
        for fn in self.__subscribers[event]:
            fn(eventData)
