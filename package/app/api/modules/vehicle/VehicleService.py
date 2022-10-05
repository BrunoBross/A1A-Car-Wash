from typing import Optional
from package.app.api.modules.user.UserDtoMapper import UserDtoMapper
from package.app.api.modules.vehicle.VehicleQuery import VehicleQuery
from package.app.api.modules.user.dto.UserDto import UserDto
from package.app.meta.Singleton import Singleton
from package.app.api.model.Vehicle import Vehicle

class VehicleService(metaclass=Singleton):
    def __init__(self):
        self.__query = VehicleQuery()
        

    def createVehicle(self, board:str):
        self.__query.createVehicle(Vehicle(numberPlate=board))


   
