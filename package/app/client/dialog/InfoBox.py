from dataclasses import dataclass, field
from package.app.client.gui.imports import Gtk


@dataclass
class InfoBoxProps:
    title: str
    content: Gtk.Box


class InfoBox(Gtk.Dialog):
    def __init__(self, parent: Gtk.Window, props: InfoBoxProps):
        super().__init__(
            props.title,
            parent,
            Gtk.DialogFlags.MODAL,
            (
                Gtk.STOCK_CANCEL,
                Gtk.ResponseType.CANCEL,
                Gtk.STOCK_OK,
                Gtk.ResponseType.OK,
            ),
        )

        self.set_resizable(False)
        self.__content = self.get_content_area()
        self.__content.add(props.content)
