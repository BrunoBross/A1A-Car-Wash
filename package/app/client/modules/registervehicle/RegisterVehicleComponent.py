from package.app.api.modules.auth.AuthController import AuthController
from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.client.event.EventEnum import EventEnum
from package.app.client.event.EventManager import EventManager
from package.app.client.state.ComponentState import ComponentState
from package.app.client.gui.imports import Gtk
from package.app.client.utils.form import getEntryBuffer
from package.app.meta.Singleton import Singleton
from package.app.api.modules.vehicle.VehicleService import VehicleService

class RegisterVehicleComponent(metaclass=Singleton):
    def __init__(self):
        self.__vehicleService = VehicleService()
        

    def createVehicle(self, board:str): 
        self.__vehicleService.createVehicle(board)

    
