from typing import Optional
from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO
from package.app.api.model.Scheduling import Scheduling
from datetime import date
from package.app import sqlalchemy_session


class SchedulingQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()
        self.__session = sqlalchemy_session

    def getAll(self) -> Optional[Scheduling]:
        return self.__dao.select(Scheduling).all()

    def getByEmployeeId(self, employeeId: int) -> Optional[Scheduling]:
        return self.__dao.select(Scheduling)\
            .where(Scheduling.employee_id == employeeId)\
            .where(Scheduling.job_state_id == 1)\
            .all()

    def updateJobStateID(self, employeeId: int, jobID: int, vehicleId: int, date: date, newJobStateId: int):
        self.__session.query(Scheduling) \
            .where(Scheduling.employee_id == employeeId)\
            .where(Scheduling.job_id == jobID)\
            .where(Scheduling.vehicle_id == vehicleId)\
            .where(Scheduling.date == date)\
            .update({"job_state_id": newJobStateId})

        self.__session.commit()
