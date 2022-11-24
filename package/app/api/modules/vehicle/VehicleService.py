from typing import List, Optional, Set

from sqlalchemy.sql.ddl import SetTableComment
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

    def getVehicles(self) -> List[VehicleDto]:
        result = list()
        for vehicle in self.__query.getVehicles():
            result.append(self.__mapper.mapVehicleToDto(vehicle))
        return result

    def createVehicle(self, vehicleDto: VehicleDto) -> Optional[VehicleDto]:
        if self.__validator.execute(vehicleDto):
            self.__query.createVehicle(self.__mapper.mapDtoToVehicle(vehicleDto))
            return vehicleDto
        return None

    def getVehicleByPlate(self, plate: str) -> Optional[VehicleDto]:
        return self.__query.getVehicleByNumberPlate(plate)

    def getVehicleById(self, id:int) -> Optional[VehicleDto]:
        return self.__query.getVehicleById(id)

    def getAllVehicles(self) -> Optional[VehicleDto]:
        return self.__query.getAllVehicles()

    def updateVehicle(self, vehicleUpdates: VehicleDto, vehicle_id: int):
        vehicleUpdatesDict = {"number_plate": vehicleUpdates.numberPlate}
        self.__query.updateVehicle(vehicleUpdatesDict, vehicle_id)