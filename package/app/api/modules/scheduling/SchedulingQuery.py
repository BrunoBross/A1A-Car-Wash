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
        except DatabaseIntegrityException:
            return None

    def getSchedulingByEmployeeIDAndDate(self, employeeId: int, startMonth:str, endMonth:str) -> Optional[Scheduling]:
        return self.__dao.select(Scheduling) \
            .where(Scheduling.employee_id == employeeId) \
            .where(Scheduling.date >= startMonth) \
            .where(Scheduling.date <= endMonth) \
            .all()

    def getSchedulingsByEmployeeId(self, employee_id):
        return self.__dao.select(Scheduling)\
            .where(Scheduling.employee_id == employee_id)\
            .where(Scheduling.job_state_id == 1)\
            .all()

    def getSchedulingsByVehicleId(self, vehicle_id):
        return self.__dao.select(Scheduling)\
            .where(Scheduling.vehicle_id == vehicle_id)\
            .where(Scheduling.job_state_id == 1)\
            .all()

    def deleteSchedulingByEmployeeId(self, employee_id):
        schedulings = self.__dao.select(Scheduling).where(Scheduling.employee_id == employee_id).all()
        for scheduling in schedulings:
            self.__dao.delete(scheduling)
