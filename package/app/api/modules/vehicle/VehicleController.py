from typing import List, Optional, Set
from package.app.api.modules.vehicle.dto.VehicleDto import VehicleDto
from package.app.decorators import post_endpoint
from package.app.meta.Singleton import Singleton
from package.app.api.modules.vehicle.VehicleService import VehicleService


class VehicleController(metaclass=Singleton):
    def __init__(self):
        self.__vehicleService = VehicleService()

    def getVehicles(self) -> List[VehicleDto]:
        return self.__vehicleService.getVehicles()

    @post_endpoint
    def createVehicle(self, vehicleDto: VehicleDto) -> Optional[VehicleDto]:
        return self.__vehicleService.createVehicle(vehicleDto)

    def getVehicleByPlate(self, plate:int) ->Optional[VehicleDto]:
        return self.__vehicleService.getVehicleByPlate(plate)

    def getVehicleById(self, id:int) -> Optional[VehicleDto]:
        return self.__vehicleService.getVehicleById(id)

    def getAllVehicles(self) -> Optional[VehicleDto]:
        return self.__vehicleService.getAllVehicles()

    def updateVehicle(self, vehicleUpdates: VehicleDto, vehicle_id: int):
        self.__vehicleService.updateVehicle( vehicleUpdates, vehicle_id)
    
    def deleteVehicle(self, vehicle_id: int):
        return self.__vehicleService.deleteVehicle(vehicle_id)