from typing import Any
from package.Config import Config
from package.app.client.gui.box.Box import Box
from package.app.client.gui.imports import Gtk
from package.app.client.layout.MainComponent import MainComponent
from package.app.client.layout.sidebar import sidebarItems
from package.app.meta.Singleton import Singleton


class MainView(metaclass=Singleton):
    def __init__(self):
        self.__component = MainComponent()

    def get(self) -> Gtk.Box:
        user = self.__component.getUserContext().get()

        box = Box(Gtk.Orientation.HORIZONTAL)
        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_UP_DOWN)
        stack.set_transition_duration(500)
        for key, value in sidebarItems.items():
            if user.role in value.roles:
                view = value.component()
                stack.add_titled(self.__wrapStackFrame(view.get()), key, key)

        switcher = Gtk.StackSwitcher(spacing=10)
        switcher.set_orientation(orientation=Gtk.Orientation.VERTICAL)
        switcher.set_stack(stack)
        stack.connect("notify::visible-child", self.__onViewChanged)

        Gtk.Widget.set_size_request(switcher, Config.SIDEBAR_WIDTH, -1)

        box.pack_start(switcher, False, True, 0)
        box.pack_default(stack)

        return box

    def __wrapStackFrame(self, frame: Gtk.Box) -> Box:
        wrapper = Box()
        wrapper.set_margin_left(5)
        wrapper.set_margin_right(5)
        wrapper.pack_default(frame)
        return wrapper

    def __onViewChanged(self, _widget: Gtk.Widget, _paramspec: Any):
        self.__component.notifyViewChange()
