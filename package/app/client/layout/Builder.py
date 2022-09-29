from package.Config import Config
from package.app.client.gui.window.Window import Window
from package.app.client.gui.window.WindowService import WindowService
from package.app.client.layout.Layout import Layout
from package.app.client.modules.login.LoginView import LoginView
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk

LAYOUT = Layout
AUTH = LoginView


class Builder(metaclass=Singleton):
    def __init__(self):
        self.__windowService = WindowService()

    def buildAuthView(self) -> Window:
        window = self.__windowService.getWindow(essential=True)
        window.add(AUTH().get())
        window.set_resizable(False)
        return window

    def buildMainView(self) -> Window:
        window = self.__windowService.getWindow(essential=True)
        window.add(LAYOUT().get())
        Gtk.Window.set_size_request(window, Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT)

        return window
