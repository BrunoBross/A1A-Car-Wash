from typing import Optional
from dataclasses import dataclass, field
from package.app.client.gui.box.Box import Box
from package.app.client.gui.imports import Gtk


@dataclass
class ModalProps:
    title: str
    content: Gtk.Box
    cancelLabel: Optional[str] = field(default=Gtk.STOCK_CANCEL)
    okLabel: Optional[str] = field(default=Gtk.STOCK_OK)


class Modal(Gtk.Dialog):
    def __init__(self, parent: Gtk.Window, props: ModalProps):
        super().__init__(
            props.title,
            parent,
            Gtk.DialogFlags.MODAL,
            (
                props.cancelLabel,
                Gtk.ResponseType.CANCEL,
                props.okLabel,
                Gtk.ResponseType.OK,
            ),
        )

        self.set_resizable(False)
        self.__content = self.get_content_area()
        self.__content.add(self.__wrapContents(props.content))
        self.show_all()

    def __wrapContents(self, content: Box) -> Box:
        content.set_margin_top(30)
        content.set_margin_right(30)
        content.set_margin_bottom(30)
        content.set_margin_left(30)
        return content
