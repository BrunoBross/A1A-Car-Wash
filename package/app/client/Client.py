from typing import Type
from package.app.api.enum.RoleEnum import RoleEnum
from package.app.client.gui.WindowService import WindowService
from package.app.client.layout.Builder import Builder
from package.app.meta.Singleton import Singleton
from package.app.template.IAppModule import IAppModule
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Client(IAppModule, metaclass=Singleton):
    def __init__(self):
        self.__windowService = WindowService()
        self.__builder = Builder()

    def start(self):
        window = self.__builder.buildView(RoleEnum.GERENTE)
        self.__windowService.displayWindow(window)
        Gtk.main()
