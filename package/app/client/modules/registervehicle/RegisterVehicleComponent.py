from package.app.api.modules.vehicle.dto.VehicleDto import VehicleDto
from package.app.client.dialog.DialogService import DialogService
from package.app.client.dialog.InfoBox import InfoBoxProps
from package.app.client.gui.box.Box import Box
from package.app.client.state.ComponentState import ComponentState
from package.app.client.utils.form import getEntryBuffer
from package.app.meta.Singleton import Singleton
from package.app.api.modules.vehicle.VehicleController import VehicleController
from package.app.client.gui.imports import Gtk
from package.app.client.modules.registervehicle.RegisterVehicleValidator import (
    RegisterVehicleValidator,
)
from package.app.validation.IValidator import IValidator


class RegisterVehicleComponent(metaclass=Singleton):
    def __init__(self):
        self.__controller = VehicleController()
        self.__validator: IValidator = RegisterVehicleValidator()
        self.__dialogService = DialogService()
        self.__state = ComponentState()

    def requestCreateVehicle(self):
        dto = VehicleDto(
            numberPlate=getEntryBuffer(
                self.__state.getReferenceById("numberPlate")
            ).upper()
        )
        if self.__validator.execute(dto):
            entity = self.__controller.createVehicle(dto)
            if entity:
                self.__displaySuccessMessage()

    def getState(self) -> ComponentState:
        return self.__state

    def __displaySuccessMessage(self):
        content = Box()
        content.pack_default(Gtk.Label("Veículo cadastrado com sucesso"))
        self.__dialogService.displayInfoBox(
            InfoBoxProps(title="Cadastro bem sucedido", content=content)
        )
