from package.Config import Config
from package.app.api.enum.RoleEnum import RoleEnum
from package.app.client.gui.box.Box import Box
from package.app.client.gui.imports import Gtk
from package.app.client.layout.sidebar import sidebarItems
from package.app.meta.Singleton import Singleton
from package.app.template.IAppComponent import IAppComponent


class MainView(IAppComponent, metaclass=Singleton):
    @staticmethod
    def get() -> Gtk.Box:
        role = RoleEnum.GERENTE  # TODO: trocar

        box = Box(Gtk.Orientation.HORIZONTAL)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_UP_DOWN)
        stack.set_transition_duration(500)
        for key, value in sidebarItems.items():
            view = value.component()
            if role in value.roles:
                stack.add_titled(view.get(), key, key)

        switcher = Gtk.StackSwitcher(spacing=10)
        switcher.set_orientation(orientation=Gtk.Orientation.VERTICAL)
        switcher.set_stack(stack)

        Gtk.Widget.set_size_request(switcher, Config.SIDEBAR_WIDTH, -1)

        box.pack_start(switcher, False, True, 0)
        box.pack_default(stack)

        return box