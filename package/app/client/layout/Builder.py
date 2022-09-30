from package.Config import Config
from package.app.client.gui.window.Window import Window
from package.app.client.gui.window.WindowService import WindowService
from package.app.client.layout.Layout import MainView
from package.app.client.modules.login.LoginEventEnum import LoginEventEnum
from package.app.client.modules.login.LoginEventManager import LoginEventManager
from package.app.client.modules.login.LoginView import LoginView
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk

LAYOUT = MainView
AUTH = LoginView


class Builder(metaclass=Singleton):
    def __init__(self):
        self.__windowService = WindowService()
        self.__mainView = self.__buildMainView()
        self.__authView = self.__buildAuthView()
        self.__eventManager = LoginEventManager()
        self.__subscribeSetup()

    def __buildAuthView(self) -> Window:
        window = self.__windowService.getWindow(essential=False)
        window.add(AUTH().get())
        window.set_resizable(False)

        return window

    def __buildMainView(self) -> Window:
        window = self.__windowService.getWindow(essential=True)
        window.add(LAYOUT().get())
        Gtk.Window.set_size_request(window, Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT)

        return window

    def __displayMainView(self):
        self.__windowService.displayWindow(self.__mainView)

    def __displayAuthView(self):
        self.__windowService.displayWindow(self.__authView)

    def __closeMainView(self):
        self.__windowService.closeWindow(self.__mainView)

    def __closeAuthView(self):
        self.__windowService.closeWindow(self.__authView)

    def __subscribeSetup(self):
        self.__eventManager.subscribe(LoginEventEnum.STARTUP, self.__displayAuthView)

        self.__eventManager.subscribe(LoginEventEnum.LOGIN, self.__displayMainView)
        self.__eventManager.subscribe(LoginEventEnum.LOGIN, self.__closeAuthView)

        self.__eventManager.subscribe(LoginEventEnum.LOGOUT, self.__displayAuthView)
        self.__eventManager.subscribe(LoginEventEnum.LOGOUT, self.__closeMainView)
