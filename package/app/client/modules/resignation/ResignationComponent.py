from traceback import print_tb
from package.app.api.modules.resignation.ResignationController import ResignationController
from package.app.client.dialog.DialogService import DialogService
from package.app.client.dialog.InfoBox import InfoBoxProps
from package.app.client.gui.box.Box import Box
from package.app.client.modules.resignation.ResignationValidator import (
    ResignationValidator,
)
from package.app.client.state.ComponentState import ComponentState
from package.app.meta.Singleton import Singleton
from package.app.client.utils.form import getEntryBuffer
from package.app.api.modules.resignation.dto.ResignationDto import ResignationDto
from package.app.client.gui.imports import Gtk
from package.app.validation.IValidator import IValidator
from datetime import datetime


class ResignationComponent(metaclass=Singleton):
    def __init__(self):
        self.__state = ComponentState()
        self.__validator: IValidator = ResignationValidator()
        self.__controller = ResignationController()
        self.__dialogService = DialogService()

    def requestRegistration(self):
        selectedEmployee = getEntryBuffer(self.__state.getReferenceById("employee"))
        selectedResignationType = getEntryBuffer(self.__state.getReferenceById("resignationType"))
        typedMemo = getEntryBuffer(self.__state.getReferenceById("memo"))

        dto = ResignationDto(
            employee = selectedEmployee,
            resignationType = selectedResignationType,
            memo = str(typedMemo),
            date = str(datetime.now())
        )

        if self.__validator.execute(dto):
            entity = self.__controller.registerResignation(dto)
            if entity:
                self.__displaySuccessMessage()

    def getState(self) -> ComponentState:
        return self.__state

    def __displaySuccessMessage(self):
        content = Box()
        content.pack_default(Gtk.Label("A dedmissão foi corretamente executada!"))
        self.__dialogService.displayInfoBox(
            InfoBoxProps(title="Demissão executada", content=content)
        )

    def getEmployees(self):
        return self.__controller.getEmployees()

    def getResignationTypes(self):
        return self.__controller.getResignationTypes()
