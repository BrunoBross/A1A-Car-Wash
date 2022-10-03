from package.Config import Config
from package.app.api.enum.RoleEnum import RoleEnum
from package.app.client.gui.box.Box import Box
from package.app.client.gui.imports import Gtk
from package.app.client.layout.MainComponent import MainComponent
from package.app.client.layout.sidebar import sidebarItems
from package.app.client.state.ComponentState import ComponentState
from package.app.meta.Singleton import Singleton
from package.app.template.IAppComponent import IAppComponent


class MainView(IAppComponent, metaclass=Singleton):  # TODO: logout
    def __init__(self):
        self.__component = MainComponent()
        self.__state = ComponentState()

    def get(self) -> Gtk.Box:
        user = self.__component.getUserContext().get()

        box = Box(Gtk.Orientation.HORIZONTAL)

        menuBar = Gtk.MenuBar()
        sessionMenu = Gtk.Menu()
        sessionMenuDropdown = Gtk.MenuItem("Session")
        sessionExit = Gtk.MenuItem("Exit session")
        sessionQuit = Gtk.MenuItem(f"Quit {Config.APP_NAME}")
        sessionAppInfo = Gtk.MenuItem("About app")
        sessionMenu.append(sessionExit)
        sessionMenu.append(sessionQuit)
        sessionMenu.append(Gtk.SeparatorMenuItem())
        sessionMenu.append(sessionAppInfo)
        sessionMenuDropdown.set_submenu(sessionMenu)
        menuBar.append(sessionMenuDropdown)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_UP_DOWN)
        stack.set_transition_duration(500)
        for key, value in sidebarItems.items():
            view = value.component()
            if user.role in value.roles:
                stack.add_titled(view.get(), key, key)

        switcher = Gtk.StackSwitcher(spacing=10)
        switcher.set_orientation(orientation=Gtk.Orientation.VERTICAL)
        switcher.set_stack(stack)

        Gtk.Widget.set_size_request(switcher, Config.SIDEBAR_WIDTH, -1)

        box.pack_start(menuBar, False, False, 0)
        box.pack_start(switcher, False, True, 0)
        box.pack_default(stack)

        return box
