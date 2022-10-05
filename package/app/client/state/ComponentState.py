from typing import Dict, Optional
from package.app.client.event.EventEnum import EventEnum
from package.app.client.event.EventManager import EventData, EventManager
from package.app.client.gui.imports import Gtk


class ComponentState:
    def __init__(self):
        self.__data: Dict[str, Gtk.Widget] = dict()
        self.__eventManager = EventManager()
        self.__setup()

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
        self.__data.clear()

    def __handleEvent(self, _: Optional[EventData]):
        self.reset()

    def __setup(self):
        self.__eventManager.subscribe(EventEnum.WINDOW_CLOSED, self.__handleEvent)
        self.__eventManager.subscribe(EventEnum.SWITCH_VIEW, self.__handleEvent)
