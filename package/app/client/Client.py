from package.app.client.event.EventEnum import EventEnum
from package.app.client.event.EventManager import EventManager
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk


class Client(metaclass=Singleton):
    def __init__(self):
        self.__eventManager = EventManager()

    def start(self):
        self.__eventManager.post(EventEnum.STARTUP)
        Gtk.main()
