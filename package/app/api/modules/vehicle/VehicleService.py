from typing import Optional
from package.app.api.modules.vehicle.VehicleDtoMapper import VehicleDtoMapper
from package.app.api.modules.vehicle.VehicleQuery import VehicleQuery
from package.app.api.modules.vehicle.VehicleValidator import VehicleValidator
from package.app.api.modules.vehicle.dto.VehicleDto import VehicleDto
from package.app.meta.Singleton import Singleton
from package.app.validation.IValidator import IValidator


class VehicleService(metaclass=Singleton):
    def __init__(self):
        self.__query = VehicleQuery()
        self.__mapper = VehicleDtoMapper()
        self.__validator: IValidator = VehicleValidator()

    def createVehicle(self, vehicleDto: VehicleDto) -> Optional[VehicleDto]:
        if self.__validator.execute(vehicleDto):
            self.__query.createVehicle(self.__mapper.mapDtoToVehicle(vehicleDto))
            return vehicleDto
        return None

    def getVehicleByPlate(self, plate:int) -> Optional[VehicleDto]:
        return self.__query.getVehicleByNumberPlate(plate)

    def getVehicleById(self, id:int) -> Optional[VehicleDto]:
        return self.__query.getVehicleById(id)