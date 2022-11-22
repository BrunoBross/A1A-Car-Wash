from typing import Optional
from package.app.api.model.Scheduling import Scheduling
from package.app.api.orm.DAO import DAO
from package.app.exception.DatabaseIntegrityException import DatabaseIntegrityException
from package.app.meta.Singleton import Singleton


class SchedulingQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()

    def getScheduling(
        self, employeeId: int, vehicleId: int, jobId: int
    ) -> Optional[Scheduling]:
        return (
            self.__dao.select(Scheduling)
            .filter(
                Scheduling.employee_id
                and Scheduling.vehicle_id == vehicleId
                and Scheduling.job_id == jobId
            )
            .first()
        )

    def createScheduling(self, scheduling):
        try:
            self.__dao.insert(scheduling)
            scheduling
        except DatabaseIntegrityException:
            return None

    def getSchedulingByEmployeeIDAndDate(self, employeeId: int, startMonth:str, endMonth:str) -> Optional[Scheduling]:
        return self.__dao.select(Scheduling) \
            .where(Scheduling.employee_id == employeeId) \
            .where(Scheduling.date >= startMonth) \
            .where(Scheduling.date <= endMonth) \
            .all()

    