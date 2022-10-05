from typing import Optional
from package.app.api.model.Vehicle import Vehicle
from package.app.api.orm.DAO import DAO
from package.app.meta.Singleton import Singleton


class VehicleQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()

    def createVehicle(self, vehicle: Vehicle):
        self.__dao.insert(vehicle)