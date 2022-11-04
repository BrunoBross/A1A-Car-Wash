from package.Config import Config
from package.app.client.event.EventEnum import EventEnum
from package.app.client.event.EventManager import EventManager
from package.app.client.state.UserContext import UserContext
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk


class Header(metaclass=Singleton):
    def __init__(self):
        self.__userContext = UserContext()
        self.__eventManager = EventManager()

    def get(self) -> Gtk.Box:
        box = Gtk.Box(Gtk.Orientation.HORIZONTAL)

        menuBar = Gtk.MenuBar()

        sessionMenu = Gtk.Menu()
        sessionMenuDropdown = Gtk.MenuItem("Sessão")
        sessionExit = Gtk.MenuItem(
            f"Sair da sessão 'ACESSO {self.__userContext.get().role.name}'"
        )
        sessionExit.connect("activate", self.__onExit)
        sessionQuit = Gtk.MenuItem(f"Sair do {Config.APP_NAME}")
        sessionQuit.connect("activate", self.__onQuit)
        sessionMenuDropdown.set_submenu(sessionMenu)
        sessionMenu.append(sessionExit)
        sessionMenu.append(sessionQuit)

        viewMenu = Gtk.Menu()
        viewMenuDropdown = Gtk.MenuItem("Mais")
        viewAppInfo = Gtk.MenuItem("Sobre o app")
        viewAppInfo.connect("activate", self.__onAppInfo)
        viewMenuDropdown.set_submenu(viewMenu)
        viewMenu.append(viewAppInfo)

        menuBar.append(sessionMenuDropdown)
        menuBar.append(viewMenuDropdown)
        box.add(menuBar)

        return box

    def __onAppInfo(self, _: Gtk.Widget) -> None:  # TODO
        print("viewing app info ...")

    def __onExit(self, _: Gtk.Widget) -> None:
        self.__eventManager.post(EventEnum.LOGOUT)

    def __onQuit(self, _: Gtk.Widget) -> None:
        Gtk.main_quit()
