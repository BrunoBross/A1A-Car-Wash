from package.app.meta.Singleton import Singleton
import gi

from package.app.template.IAppComponent import IAppComponent

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class LoginView(IAppComponent, metaclass=Singleton):
    @staticmethod
    def get() -> Gtk.Box:
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        label = Gtk.Label()
        label.set_text("Hello!")
        box.pack_start(label, False, False, 0)

        return box
