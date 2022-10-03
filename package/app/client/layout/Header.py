from package.Config import Config
from package.app.client.event.EventEnum import EventEnum
from package.app.client.event.EventManager import EventManager
from package.app.client.state.UserContext import UserContext
from package.app.meta.Singleton import Singleton
from package.app.template.IAppComponent import IAppComponent
from package.app.client.gui.imports import Gtk


class Header(IAppComponent, metaclass=Singleton):
    def __init__(self):
        self.__userContext = UserContext()
        self.__eventManager = EventManager()

    def get(self) -> Gtk.Box:
        box = Gtk.Box(Gtk.Orientation.HORIZONTAL)

        menuBar = Gtk.MenuBar()

        sessionMenu = Gtk.Menu()
        sessionMenuDropdown = Gtk.MenuItem("Session")

        sessionExit = Gtk.MenuItem(f"Exit session '{self.__userContext.get().role}'")
        sessionExit.connect("activate", self.__onExit)

        sessionQuit = Gtk.MenuItem(f"Quit {Config.APP_NAME}")
        sessionQuit.connect("activate", self.__onQuit)

        sessionAppInfo = Gtk.MenuItem("About app")

        sessionMenuDropdown.set_submenu(sessionMenu)

        sessionMenu.append(sessionExit)
        sessionMenu.append(sessionQuit)
        sessionMenu.append(Gtk.SeparatorMenuItem())
        sessionMenu.append(sessionAppInfo)

        menuBar.append(sessionMenuDropdown)

        box.add(menuBar)

        return box

    def __onExit(self, _: Gtk.Widget) -> None:
        self.__eventManager.post(EventEnum.LOGOUT)

    def __onQuit(self, _: Gtk.Widget) -> None:
        Gtk.main_quit()
