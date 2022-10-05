from package.app.api.modules.vehicle.dto.VehicleDto import VehicleDto
from package.app.meta.Singleton import Singleton
from package.app.api.modules.vehicle.VehicleService import VehicleService


class VehicleController(metaclass=Singleton):
    def __init__(self):
        self.__vehicleService = VehicleService()

    def requestCreateVehicle(self, vehicleDto: VehicleDto):
        self.__vehicleService.createVehicle(vehicleDto)
