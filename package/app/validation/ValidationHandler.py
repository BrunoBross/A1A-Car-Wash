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
            content = self.__getDialogLayout()
            for error in validation.errors:
                content.pack_default(Gtk.Label(error))
            self.__dialogService.displayInfoBox(
                InfoBoxProps(title="Erros de Validação", content=content)
            )

    def __getDialogLayout(self) -> Box:
        layout = Box()
        layout.set_orientation(orientation=Gtk.Orientation.VERTICAL)
        return layout

    def __subscribeSetup(self):
        self.__eventManager.subscribe(EventEnum.VALIDATION, self.__showErrors)
