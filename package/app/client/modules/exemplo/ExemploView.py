from package.app.client.modules.exemplo.ExemploComponent import ExemploComponent
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk


class ExemploView(metaclass=Singleton):
    def __init__(self):
        self.__component = ExemploComponent()

    def get(self) -> Gtk.Box:
        text = self.__component.getText()

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        label = Gtk.Label()
        label.set_text(text)
        box.pack_start(label, False, False, 0)

        return box
