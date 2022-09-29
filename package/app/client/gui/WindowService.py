from typing import Type
from package.app.meta.Singleton import Singleton
from package.app.client.gui.Window import Window
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class WindowService(metaclass=Singleton):
    def getWindow(self) -> Type[Gtk.Window]:
        window = Window()
        window.connect("destroy", Gtk.main_quit)
        return window

    def displayWindow(self, window: Type[Gtk.Window]) -> None:
        window.show_all()
