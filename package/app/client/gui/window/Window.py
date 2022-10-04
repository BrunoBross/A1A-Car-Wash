from package.Config import Config
from package.app.client.gui.imports import Gtk


class Window(Gtk.Window):
    def __init__(self):
        super().__init__(title=Config.APP_NAME)
        self.set_border_width(Config.BORDER_WIDTH)
