from typing import List, Optional
from package.app.api.model.Vehicle import Vehicle
from package.app.api.orm.DAO import DAO
from package.app.exception.DatabaseIntegrityException import DatabaseIntegrityException
from package.app.meta.Singleton import Singleton
from package.app import sqlalchemy_session
from sqlalchemy import delete

class VehicleQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()
        self.__session = sqlalchemy_session

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
        return self.__dao.select(Vehicle).where(Vehicle.numberPlate == numberPlate).first()

    def getVehicleById(self, id:int) -> Optional[Vehicle]:
        return self.__dao.select(Vehicle).where(Vehicle.id == id).first()

    def getAllVehicles(self) -> Optional[Vehicle]:
        return self.__dao.select(Vehicle).all()

    def updateVehicle(self, vehicleUpdates: dict, vehicle_id: int):
            self.__session.query(Vehicle).where(Vehicle.id == vehicle_id).update(vehicleUpdates)
            self.__session.commit()
    
    def deleteVehicleById(self, vehicle_id):
        return self.__dao.delete(self.__dao.select(Vehicle).where(Vehicle.id == vehicle_id).first())