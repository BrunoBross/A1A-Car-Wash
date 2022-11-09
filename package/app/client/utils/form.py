from typing import Any, Optional
from package.app.client.gui.imports import Gtk


def getEntryBuffer(entry: Gtk.Widget) -> str:
    return Gtk.EntryBuffer.get_text(Gtk.Entry.get_buffer(entry))


def safeCastIdToInt(id: Optional[Any]) -> int:
    DEFAULT = -1
    try:
        return int(id)
    except TypeError:
        return DEFAULT
