from package.app.meta.Singleton import Singleton
from package.app.api.modules.vehicle.VehicleService import VehicleService


class VehicleController(metaclass=Singleton):
    def __init__(self):
        self.__vehicleService = VehicleService()

    def createVehicle(self, board:str):     
        self.__vehicleService.createVehicle(board)
        
    
        
