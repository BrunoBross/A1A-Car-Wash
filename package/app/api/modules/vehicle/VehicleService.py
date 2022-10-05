from typing import Optional
from package.app.api.modules.vehicle.VehicleDtoMapper import VehicleDtoMapper
from package.app.api.modules.vehicle.VehicleQuery import VehicleQuery
from package.app.api.modules.vehicle.dto.VehicleDto import VehicleDto
from package.app.meta.Singleton import Singleton


class VehicleService(metaclass=Singleton):
    def __init__(self):
        self.__query = VehicleQuery()
        self.__mapper = VehicleDtoMapper()

    def createVehicle(self, vehicleDto: VehicleDto) -> Optional[VehicleDto]:
        vehicle = self.__query.createVehicle(self.__mapper.mapDtoToVehicle(vehicleDto))
        if vehicle:
            return self.__mapper.mapVehicleToDto(vehicle)
        return None
