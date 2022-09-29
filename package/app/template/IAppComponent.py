from __future__ import annotations
from abc import abstractmethod
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class IAppComponent:
    @abstractmethod
    def get() -> Gtk.Box:
        pass
