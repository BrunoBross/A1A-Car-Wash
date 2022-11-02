from package.app.client.dialog.DialogService import DialogService
from package.app.client.dialog.InfoBox import InfoBoxProps
from package.app.client.event.EventEnum import EventEnum
from package.app.client.event.EventManager import EventData, EventManager
from package.app.client.gui.box.Box import Box
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject
from package.app.client.gui.imports import Gtk


class ValidationHandler(metaclass=Singleton):
    def __init__(self):
        self.__dialogService = DialogService()
        self.__eventManager = EventManager()
        self.__subscribeSetup()

    def __showErrors(self, data: EventData):
        validation: ValidationObject = data.data
        if not validation.isValid:
            content = Box()
            content.pack_default(Gtk.Label("lolol"))
            self.__dialogService.displayInfoBox(
                InfoBoxProps(title="errors", content=content)
            )

    def __subscribeSetup(self):
        self.__eventManager.subscribe(EventEnum.VALIDATION, self.__showErrors)
