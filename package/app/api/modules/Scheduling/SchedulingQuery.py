from typing import Optional
from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO
from package.app.api.model.Scheduling import Scheduling


class SchedulingQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()

    def getAll(self) -> Optional[Scheduling]:
        return self.__dao.select(Scheduling).all()

    def getByEmployeeId(self, employeeId:int) -> Optional[Scheduling]:
        return self.__dao.select(Scheduling).where(Scheduling.employee_id == employeeId)