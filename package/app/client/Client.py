from package.app.client.gui.window.WindowService import WindowService
from package.app.client.layout.Builder import Builder
from package.app.client.state.UserContext import UserContext
from package.app.meta.Singleton import Singleton
from package.app.template.IAppModule import IAppModule
from package.app.client.gui.imports import Gtk


class Client(IAppModule, metaclass=Singleton):
    def __init__(self):
        self.__userContext = UserContext()
        self.__windowService = WindowService()
        self.__builder = Builder()

    def start(self):
        self.__getAuth()
        self.__windowService.displayWindow(self.__builder.buildMainView())
        Gtk.main()

    def __getAuth(self):
        self.__windowService.displayWindow(self.__builder.buildAuthView())
