from typing import Dict, Optional
from package.app.client.gui.imports import Gtk


class ComponentState:
    def __init__(self):
        self.__data: Dict = {}

    def addReference(self, key: str, widget: Gtk.Widget) -> bool:
        if key in self.__data.keys():
            return False
        self.__data[key] = widget
        return True

    def removeReference(self, key: str) -> None:
        self.__data.pop(key)

    def getReferenceById(self, key) -> Optional[Gtk.Widget]:
        return self.__data[key]

    def getKeys(self):
        return self.__data.keys()

    def reset(self):
        self.__data = {}
