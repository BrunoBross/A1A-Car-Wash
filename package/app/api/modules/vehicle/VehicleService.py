from package.app.api.modules.vehicle.VehicleDtoMapper import VehicleDtoMapper
from package.app.api.modules.vehicle.VehicleQuery import VehicleQuery
from package.app.api.modules.vehicle.dto.VehicleDto import VehicleDto
from package.app.meta.Singleton import Singleton
from package.app.api.model.Vehicle import Vehicle


class VehicleService(metaclass=Singleton):
    def __init__(self):
        self.__query = VehicleQuery()
        self.__mapper = VehicleDtoMapper()

    def createVehicle(self, vehicleDto: VehicleDto):
        self.__query.createVehicle(self.__mapper.mapDtoToVehicle(vehicleDto))
