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


class ResignationComponent(metaclass=Singleton):
    def __init__(self):
        self.__state = ComponentState()
        self.__validator: IValidator = ResignationValidator()
        self.__controller = ResignationController()
        self.__dialogService = DialogService()

    # NEED FIXING
    def requestRegistration(self):
        description = getEntryBuffer(self.__state.getReferenceById("resignationName"))
        cost_value = getEntryBuffer(self.__state.getReferenceById("resignationValue"))

        try:
            dto = ResignationDto(
                description=description.upper(),
                cost_value=float(cost_value),
            )

        except ValueError:
            if cost_value == "":
                dto = ResignationDto(
                    description=description.upper(),
                    cost_value=0,
                )
            else:
                dto = ResignationDto(
                    description=description.upper(),
                    cost_value="invalid_cost",
                )

        if self.__validator.execute(dto):
            entity = self.__controller.registerResignation(dto)
            if entity:
                self.__displaySuccessMessage()

    def getState(self) -> ComponentState:
        return self.__state

    def __displaySuccessMessage(self):
        content = Box()
        content.pack_default(Gtk.Label("Serviço cadastrado com sucesso"))
        self.__dialogService.displayInfoBox(
            InfoBoxProps(title="Cadastro bem sucedido", content=content)
        )
