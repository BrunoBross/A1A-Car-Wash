from package.app.api.modules.auth.AuthController import AuthController
from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.client.event.EventEnum import EventEnum
from package.app.client.event.EventManager import EventManager
from package.app.client.state.ComponentState import ComponentState
from package.app.client.gui.imports import Gtk
from package.app.client.utils.form import getEntryBuffer
from package.app.meta.Singleton import Singleton
#from package.app.api.modules.vehicle.VehicleService import VehicleService
from package.app.api.modules.vehicle.VehicleController import VehicleController
from package.app.client.modules.registervehicle.RegisterVehicleValidator import RegisterVehicleValidator

class RegisterVehicleComponent(metaclass=Singleton):
    def __init__(self):
        self.__vehicleController = VehicleController()
        self.__vehicleValidator = RegisterVehicleValidator()

    def createVehicle(self, numberPlate:str): 
        if self.__vehicleValidator.execute(numberPlate):
            self.__vehicleController.createVehicle(numberPlate)
        else:
            print("ATENÇAO! Placa invalida, por favor insira outro valor!")
    
