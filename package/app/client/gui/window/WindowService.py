from typing import Optional
from package.app.client.gui.window.InstanceManager import InstanceManager
from package.app.meta.Singleton import Singleton
from package.app.client.gui.window.Window import Window
from package.app.client.gui.imports import Gtk


class WindowService(metaclass=Singleton):
    def __init__(self):
        self.__instanceManager = InstanceManager()

    def getWindow(self, essential: bool = True) -> Window:
        window = Window()
        if essential:
            window.connect("destroy", Gtk.main_quit)
        return window

    def displayWindow(self, window: Optional[Window]) -> None:
        if window:
            window.show_all()
            self.__instanceManager.addInstance(window)
            window.connect("destroy", self.__instanceManager.terminateInstance)

    def closeWindow(self, window: Optional[Window]) -> None:
        if window:
            Gtk.Window.close(window)
