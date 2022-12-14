from typing import Optional
from package.Config import Config
from package.app.client.defaults import AUTH, HEAD, MAIN
from package.app.client.gui.window.Window import Window
from package.app.client.gui.window.WindowService import WindowService
from package.app.client.event.EventEnum import EventEnum
from package.app.client.event.EventManager import EventData, EventManager
from package.app.client.state.UserContext import UserContext
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk


class Builder(metaclass=Singleton):
    def __init__(self):
        self.__windowService = WindowService()
        self.__eventManager = EventManager()
        self.__userContext = UserContext()
        self.__mainView: Optional[Window]
        self.__authView: Optional[Window]

        self.__subscribeSetup()

    def __buildAuthView(self) -> Window:
        window = self.__windowService.getWindow(essential=False)
        window.add(AUTH.get())
        window.set_resizable(False)
        self.__authView = window

        return window

    def __buildMainView(self) -> Window:
        window = self.__windowService.getWindow(essential=False)
        header = Gtk.HeaderBar()
        header.set_title(
            f"{Config.APP_NAME} - ACESSO {self.__userContext.get().role.name}"
        )
        header.set_show_close_button(True)
        header.pack_start(HEAD.get())
        window.set_titlebar(header)

        window.add(MAIN.get())
        Gtk.Window.set_size_request(window, Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT)
        self.__mainView = window

        return window

    def __displayMainView(self, _: Optional[EventData] = None):
        window = self.__buildMainView()
        self.__windowService.displayWindow(window)
        self.__eventManager.post(EventEnum.WINDOW_OPENED, window)

    def __displayAuthView(self, _: Optional[EventData] = None):
        window = self.__buildAuthView()
        self.__windowService.displayWindow(window)
        self.__eventManager.post(EventEnum.WINDOW_OPENED, window)

    def __closeMainView(self, _: Optional[EventData] = None):
        self.__windowService.closeWindow(self.__mainView)
        self.__mainView = None
        self.__eventManager.post(EventEnum.WINDOW_CLOSED)

    def __closeAuthView(self, _: Optional[EventData] = None):
        self.__windowService.closeWindow(self.__authView)
        self.__authView = None
        self.__eventManager.post(EventEnum.WINDOW_CLOSED)

    def __onLogin(self, _: EventData):
        self.__closeAuthView()
        self.__displayMainView()

    def __onLogout(self, _: EventData):
        self.__closeMainView()
        self.__displayAuthView()

    def __subscribeSetup(self):
        self.__eventManager.subscribe(EventEnum.STARTUP, self.__displayAuthView)
        self.__eventManager.subscribe(EventEnum.CONTEXT_SET, self.__onLogin)
        self.__eventManager.subscribe(EventEnum.LOGOUT, self.__onLogout)
