from dataclasses import dataclass
from package.app.client.gui.box.Box import Box
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
                Gtk.STOCK_OK,
                Gtk.ResponseType.OK,
            ),
        )

        self.set_resizable(False)
        self.__content = self.get_content_area()
        self.__content.add(self.__wrapContents(props.content))
        self.show_all()

    def __wrapContents(self, content: Box) -> Box:
        content.set_margin_top(5)
        content.set_margin_right(5)
        content.set_margin_bottom(5)
        content.set_margin_left(5)
        return content
