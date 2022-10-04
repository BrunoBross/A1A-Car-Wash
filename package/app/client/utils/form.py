from package.app.client.gui.imports import Gtk


def getEntryBuffer(entry: Gtk.Widget) -> str:
    return Gtk.EntryBuffer.get_text(Gtk.Entry.get_buffer(entry))
