from datetime import datetime
from package.Config import Config
from package.app.client.event.EventEnum import EventEnum
from package.app.client.event.EventManager import EventData, EventManager
from package.app.meta.Singleton import Singleton


class EventLogger(metaclass=Singleton):
    def __init__(self):
        self.__eventManager = EventManager()
        self.__setup()

    def __setup(self):
        for event in EventEnum:
            self.__eventManager.subscribe(event, self.__log)

    def __log(self, data: EventData) -> None:
        Config.LOG_OUT(
            f"[EVENT LOGGER] [{datetime.now()}] [EVENT: {data.event}; DATA: {data.data}]"
        )
