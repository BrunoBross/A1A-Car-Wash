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
from package.app.exception.DatabaseIntegrityException import DatabaseIntegrityException
from package.app.client.dialog.Modal import ModalProps


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
                self.__displaySuccessMessage("Veiculo cadastrado com sucesso", "Cadastro bem sucedido")

    def getState(self) -> ComponentState:
        return self.__state

    def __displaySuccessMessage(self, message: str, title_message: str):
        content = Box()
        content.pack_default(Gtk.Label(message))
        self.__dialogService.displayInfoBox(
            InfoBoxProps(title=title_message, content=content)
        )

    def getAllVehicles(self) -> VehicleDto:
        return self.__controller.getAllVehicles()

    def getVehicleList(self):
        vehicles = self.__controller.getAllVehicles()
        vehicleList = []
        for vehicle in vehicles:
            vehicleList.append([vehicle.id, vehicle.numberPlate])
        return vehicleList

    def requestEditVehicle(self, vehicle: list):
        if vehicle is None:
            return

        vehicle_id = vehicle[0]
        vehicleDto = VehicleDto(
            numberPlate=getEntryBuffer(
                self.__state.getReferenceById("numberPlateEdit")
            ).upper()
       )
        if self.__validator.execute(vehicleDto):
            try:
                self.__controller.updateVehicle(vehicleDto, vehicle_id)
                return self.__displaySuccessMessage("Veiculo editado com sucesso", "Edi????o bem sucedida")
            except DatabaseIntegrityException as e:
                    print(e)
                    return self.__displaySuccessMessage("Erro na edi????o, tente novamente", "Erro")

    def requestDeleteVehicle(self, vehicle:list):
        vehicle_id = vehicle[0]
        if self.__displayConfirmBox(vehicle, "deletar"):
            try:
                if self.__controller.deleteVehicle(vehicle_id):
                    return self.__displaySuccessMessage("Veiculo deletado com sucesso", "Dele????o bem sucedida")
                return self.__displaySuccessMessage("O veiculo possui agendamentos cadastrados", "Erro")
            except DatabaseIntegrityException as e:
                print(e)
                return self.__displaySuccessMessage("Erro na dele??ao, tente novamente", "Erro")
        else:
            return
    
    def __displayConfirmBox(self, vehicle: list, label: str):
        content = Box()
        content.pack_default(Gtk.Label(f"Tem certeza que voc?? deseja {label} o veiculo com a placa {vehicle[1]}?"))
        return self.__dialogService.displayModal(
            ModalProps(title="Confirma????o", content=content, cancelLabel="Cancelar", okLabel="Confirmar")
        )
