from typing import List, Optional
from package.app.api.model.Vehicle import Vehicle
from package.app.api.orm.DAO import DAO
from package.app.exception.DatabaseIntegrityException import DatabaseIntegrityException
from package.app.meta.Singleton import Singleton


class VehicleQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()

    def getVehicle(self, id: int) -> Optional[Vehicle]:
        return self.__dao.get(Vehicle, id)

    def getVehicles(self) -> List[Vehicle]:
        return self.__dao.select(Vehicle).all()

    def createVehicle(self, vehicle: Vehicle) -> Optional[Vehicle]:
        try:
            self.__dao.insert(vehicle)
            return vehicle
        except DatabaseIntegrityException:
            return None

    def getVehicleByNumberPlate(self, numberPlate: str) -> Optional[Vehicle]:
        return (
            self.__dao.select(Vehicle).where(Vehicle.numberPlate == numberPlate).first()
        )
