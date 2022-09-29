from __future__ import annotations
from abc import abstractmethod
from package.app.client.gui.imports import Gtk


class IAppComponent:
    @abstractmethod
    def get() -> Gtk.Box:
        pass
