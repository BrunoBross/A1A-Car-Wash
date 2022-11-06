from typing import Optional
from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO
from package.app.api.model.Scheduling import Scheduling
from datetime import date


class SchedulingQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()

    def getAll(self) -> Optional[Scheduling]:
        return self.__dao.select(Scheduling).all()

    def getByEmployeeId(self, employeeId:int) -> Optional[Scheduling]:
        return self.__dao.select(Scheduling).where(Scheduling.employee_id == employeeId)
    
    def updateJobStateID(self, employeeId:int, jobID: int, vehicleId:int, date:date, newJobStateId: int):
        
        pass
        #pegar um scheduling que tenha o mesmo, employye, job, vehicle, date e colocar o job state dele com o novo jobstate
        #Update(scheduling).where(compara).values(scheduling.jobState = newjobstate)