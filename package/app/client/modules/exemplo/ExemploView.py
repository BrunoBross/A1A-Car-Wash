from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk
from package.app.template.IAppComponent import IAppComponent


class ExemploView(IAppComponent, metaclass=Singleton):
    def get(self) -> Gtk.Box:
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        label = Gtk.Label()
        label.set_text("Hello!")
        box.pack_start(label, False, False, 0)

        return box
