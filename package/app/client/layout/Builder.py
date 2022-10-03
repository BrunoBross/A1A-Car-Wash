from package.Config import Config
from package.app.client.defaults import AUTH, MAIN
from package.app.client.gui.window.Window import Window
from package.app.client.gui.window.WindowService import WindowService
from package.app.client.event.EventEnum import EventEnum
from package.app.client.event.EventManager import EventData, EventManager
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk


class Builder(metaclass=Singleton):
    def __init__(self):
        self.__windowService = WindowService()
        self.__mainView = self.__buildMainView()
        self.__authView = self.__buildAuthView()
        self.__eventManager = EventManager()
        self.__subscribeSetup()

    def __buildAuthView(self) -> Window:
        window = self.__windowService.getWindow(essential=False)
        window.add(AUTH.get())
        window.set_resizable(False)

        return window

    def __buildMainView(self) -> Window:
        window = self.__windowService.getWindow(essential=True)
        window.add(MAIN.get())
        Gtk.Window.set_size_request(window, Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT)

        return window

    def __displayMainView(self, _: EventData):
        self.__windowService.displayWindow(self.__mainView)

    def __displayAuthView(self, _: EventData):
        self.__windowService.displayWindow(self.__authView)

    def __closeMainView(self, _: EventData):
        self.__windowService.closeWindow(self.__mainView)

    def __closeAuthView(self, _: EventData):
        self.__windowService.closeWindow(self.__authView)

    def __subscribeSetup(self):
        self.__eventManager.subscribe(EventEnum.STARTUP, self.__displayAuthView)
        self.__eventManager.subscribe(EventEnum.LOGIN, self.__displayMainView)
        self.__eventManager.subscribe(EventEnum.LOGIN, self.__closeAuthView)
        self.__eventManager.subscribe(EventEnum.LOGOUT, self.__displayAuthView)
        self.__eventManager.subscribe(EventEnum.LOGOUT, self.__closeMainView)
