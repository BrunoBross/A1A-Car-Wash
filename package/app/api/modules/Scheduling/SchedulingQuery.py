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
        return self.__dao.select(Scheduling).where(Scheduling.employee_id == employeeId)

    def updateJobStateID(self, employeeId: int, jobID: int, vehicleId: int, date: date, newJobStateId: int):
        print(employeeId)
        print(jobID)
        print(vehicleId)
        print(date)
        self.__session.query(Scheduling) \
            .filter(Scheduling.employee_id == employeeId and
                    Scheduling.job_id == jobID and
                    Scheduling.vehicle_id == vehicleId and
                    Scheduling.date == date) \
            .update({"job_state_id": newJobStateId})

        self.__session.commit()
