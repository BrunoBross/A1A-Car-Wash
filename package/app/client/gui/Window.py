import gi

from package.Config import Config

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Window(Gtk.Window):
    def __init__(self):
        super().__init__(title=Config.APP_NAME)
        self.set_border_width(Config.BORDER_WIDTH)
