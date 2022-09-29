from package.app.meta.Singleton import Singleton
from package.app.client.gui.window.Window import Window
from package.app.client.gui.imports import Gtk


class WindowService(metaclass=Singleton):
    def getWindow(self, essential: bool = True) -> Window:
        window = Window()
        if essential:
            window.connect("destroy", Gtk.main_quit)
        return window

    def displayWindow(self, window: Window) -> None:
        window.show_all()

    def closeWindow(self, window: Window) -> None:
        Gtk.Window.close(window)
