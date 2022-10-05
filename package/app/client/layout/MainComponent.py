from package.app.client.event.EventEnum import EventEnum
from package.app.client.event.EventManager import EventManager
from package.app.client.state.UserContext import UserContext
from package.app.meta.Singleton import Singleton


class MainComponent(metaclass=Singleton):
    def __init__(self):
        self.__userContext = UserContext()
        self.__eventManager = EventManager()

    def getUserContext(self):
        return self.__userContext

    def notifyViewChange(self):
        self.__eventManager.post(EventEnum.SWITCH_VIEW)
