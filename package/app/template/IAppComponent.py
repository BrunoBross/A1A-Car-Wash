from __future__ import annotations
from abc import abstractmethod
from typing import Any, Optional
from package.app.client.gui.imports import Gtk


class IAppComponent:
    @abstractmethod
    def get(_: Optional[Any]) -> Gtk.Box:
        pass
