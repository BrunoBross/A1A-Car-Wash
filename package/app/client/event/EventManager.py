from dataclasses import dataclass
from datetime import datetime
from typing import Any, Callable, Dict, Optional, Set
from package.Config import Config
from package.app.client.event.EventEnum import EventEnum
from package.app.meta.Singleton import Singleton


@dataclass
class EventData:
    data: Optional[Any]
    event: EventEnum


EventHandlerCallback = Callable[[EventData], Optional[Any]]


class EventManager(metaclass=Singleton):
    def __init__(self):
        self.__subscribers: Dict[EventEnum, Set[EventHandlerCallback]] = dict()

    def subscribe(self, event: EventEnum, callback: EventHandlerCallback):
        if event not in self.__subscribers.keys():
            self.__subscribers[event] = set()
            self.__subscribers[event].add(EventManager.Logger.log)
        self.__subscribers[event].add(callback)

    def unsubscribe(self, event: EventEnum, callback: EventHandlerCallback):
        self.__subscribers[event].remove(callback)

    def post(self, event: EventEnum, data: Optional[Any] = None):
        if event not in self.__subscribers.keys():
            self.__subscribers[event] = set()
        eventData = EventData(data=data, event=event)
        for fn in self.__subscribers[event]:
            fn(eventData)

    class Logger(metaclass=Singleton):
        @staticmethod
        def log(data: EventData) -> None:
            Config.LOG_OUT(
                f"[EVENT LOGGER] [{datetime.now()}] [EVENT: {data.event}; DATA: {data.data}]"
            )
