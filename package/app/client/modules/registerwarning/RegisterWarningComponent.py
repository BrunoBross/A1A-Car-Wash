from dataclasses import dataclass
from typing import List
from package.app.api.modules.warning.WarningController import WarningController
from package.app.api.modules.warning.dto.WarningDto import WarningDto
from package.app.client.dialog.DialogService import DialogService
from package.app.client.dialog.InfoBox import InfoBoxProps
from package.app.client.dialog.Modal import ModalProps
from package.app.client.event.EventManager import EventManager
from package.app.client.gui.box.Box import Box
from package.app.client.gui.imports import Gtk
from package.app.client.modules.registerwarning.RegisterWarningValidator import (
    RegisterWarningValidator,
)
from package.app.client.state.ComponentState import ComponentState
from package.app.client.utils.form import getEntryBuffer
from package.app.exception.DatabaseIntegrityException import DatabaseIntegrityException
from package.app.meta.Singleton import Singleton
from package.app.validation.IValidator import IValidator


@dataclass
class RegisterWarningComponentInfo:
    existingWarnings: List[WarningDto]


class RegisterWarningComponent(metaclass=Singleton):
    def __init__(self):
        self.__eventManager = EventManager()
        self.__validator: IValidator = RegisterWarningValidator()
        self.__controller = WarningController()
        self.__state = ComponentState()
        self.__dialogService = DialogService()

    def fetchInfo(self) -> RegisterWarningComponentInfo:
        return RegisterWarningComponentInfo(
            existingWarnings=self.__controller.getWarnings()
        )

    @property
    def eventManager(self) -> EventManager:
        return self.__eventManager

    def getState(self) -> ComponentState:
        return self.__state

    def requestRegisterWarning(self) -> None:
        print("in : RegisterWarningComponent::requestRegisterWarning")
        warningDto = WarningDto(
            description=getEntryBuffer(self.__state.getReferenceById("description")),
        )

        if self.__validator.execute(warningDto):
            entity = self.__controller.registerWarning(warningDto=warningDto)
            if entity:
                self.__displayInfoModal(
                    "Aviso cadastrado com sucesso", "Cadastro bem sucedido"
                )

    def requestEditWarning(self, warning: WarningDto) -> None:
        print(warning)
        if warning is None:
            self.__displayInfoModal("Nenhum aviso selecionado", "Erro")
            return

        warningDto = WarningDto(
            description=getEntryBuffer(
                self.__state.getReferenceById("descriptionEdit")
            ),
        )

        if self.__validator.execute(warningDto):
            if self.__displayConfirmBox():
                try:
                    self.__controller.editWarning(
                        warningDto=warningDto, warningId=warning
                    )
                    return self.__displayInfoModal(
                        "Aviso editado com sucesso", "Edição bem sucedida"
                    )
                except DatabaseIntegrityException:
                    return self.__displayInfoModal(
                        "Erro na edição, tente novamente", "Erro"
                    )
            else:
                return

    def requestDeleteWarning(self, warningId: int) -> None:
        print("in : RegisterWarningComponent::requestDeleteWarning")
        if self.__displayConfirmBox():
            try:
                if self.__controller.deleteWarning(warningId):
                    return self.__displayInfoModal(
                        "Aviso deletado com sucesso", "Deleção bem sucedida"
                    )
            except DatabaseIntegrityException:
                return self.__displayInfoModal(
                    "Erro na deleçao, tente novamente", "Erro"
                )
        else:
            return

    def __displayInfoModal(self, message: str, title_message: str):
        content = Box()
        content.pack_default(Gtk.Label(message))
        self.__dialogService.displayInfoBox(
            InfoBoxProps(title=title_message, content=content)
        )

    def __displayConfirmBox(self):
        content = Box()
        content.pack_default(Gtk.Label(f"Tem certeza que você deseja editar o aviso?"))
        return self.__dialogService.displayModal(
            ModalProps(
                title="Confirmação",
                content=content,
                cancelLabel="Cancelar",
                okLabel="Confirmar",
            )
        )
