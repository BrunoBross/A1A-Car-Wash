from package.app.api.modules.vehicle.dto.VehicleDto import VehicleDto
from package.app.client.state.ComponentState import ComponentState
from package.app.client.utils.form import getEntryBuffer
from package.app.meta.Singleton import Singleton
from package.app.api.modules.vehicle.VehicleController import VehicleController
from package.app.client.modules.registervehicle.RegisterVehicleValidator import (
    RegisterVehicleValidator,
)


class RegisterVehicleComponent(metaclass=Singleton):
    def __init__(self):
        self.__controller = VehicleController()
        self.__validator = RegisterVehicleValidator()
        self.__state = ComponentState()

    def requestCreateVehicle(self):  # TODO: mensagens validacao/ sucesso em modal
        dto = VehicleDto(
            numberPlate=getEntryBuffer(self.__state.getReferenceById("numberPlate"))
        )
        if self.__validator.execute(dto):
            self.__controller.requestCreateVehicle()
        else:
            print("ATENÇAO! Placa invalida, por favor insira outro valor!")

    def getState(self) -> ComponentState:
        return self.__state
