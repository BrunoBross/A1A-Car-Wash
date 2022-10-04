from __future__ import annotations
from typing import Protocol
from package.app.client.gui.imports import Gtk


class IAppComponent(Protocol):
    def get(self) -> Gtk.Box:
        ...
