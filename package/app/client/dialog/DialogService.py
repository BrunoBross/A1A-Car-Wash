from package.app.client.dialog.InfoBox import InfoBox, InfoBoxProps
from package.app.client.dialog.Modal import Modal, ModalProps
from package.app.client.event.EventEnum import EventEnum
from package.app.client.event.EventManager import EventData, EventManager
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk

RESPONSE_MAP = {Gtk.ResponseType.OK: True, Gtk.ResponseType.CANCEL: False}


class DialogService(metaclass=Singleton):
    def __init__(self):
        self.__currentWindow: Gtk.Window
        self.__eventManager = EventManager()
        self.__subscribeSetup()

    def displayModal(self, props: ModalProps) -> bool:
        modal = Modal(self.__currentWindow, props)
        response = modal.run()
        modal.destroy()
        return RESPONSE_MAP[response]

    def displayInfoBox(self, props: InfoBoxProps) -> None:
        infoBox = InfoBox(self.__currentWindow, props)
        infoBox.run()
        infoBox.destroy()

    def __setCurrentWindow(self, data: EventData):
        self.__currentWindow = data.data

    def __subscribeSetup(self):
        self.__eventManager.subscribe(EventEnum.WINDOW_OPENED, self.__setCurrentWindow)
