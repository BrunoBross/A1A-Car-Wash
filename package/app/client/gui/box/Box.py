from typing import Type
from package.app.client.gui.imports import Gtk


class Box(Gtk.Box):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pack_default(self, widget) -> Type[object]:
        return self.pack_start(widget, True, True, 0)
