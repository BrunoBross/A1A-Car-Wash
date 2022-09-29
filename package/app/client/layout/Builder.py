from package.Config import Config
from package.app.api.enum.RoleEnum import RoleEnum
from package.app.client.gui.WindowService import WindowService
from package.app.client.layout.sidebar import sidebarItems
from package.app.meta.Singleton import Singleton
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Builder(metaclass=Singleton):
    def __init__(self):
        self.__windowService = WindowService()

    def buildView(self, role: RoleEnum) -> Gtk.Window:
        window = self.__windowService.getWindow()
        box = Gtk.Box(Gtk.Orientation.HORIZONTAL)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_UP_DOWN)
        stack.set_transition_duration(500)
        for key, value in sidebarItems.items():
            print(key, value)
            if role in value.roles:
                stack.add_titled(value.component.get(), key, key)

        switcher = Gtk.StackSwitcher()
        switcher.set_orientation(orientation=Gtk.Orientation.VERTICAL)
        switcher.set_stack(stack)

        box.pack_start(switcher, False, True, 0)
        box.pack_start(stack, True, True, 0)

        Gtk.Widget.set_size_request(switcher, Config.SIDEBAR_WIDTH, -1)
        Gtk.Window.set_size_request(window, Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT)

        window.add(box)

        return window
