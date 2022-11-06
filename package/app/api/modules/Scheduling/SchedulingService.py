from package.app.meta.Singleton import Singleton
from package.app.api.modules.Scheduling.SchedulingQuery import SchedulingQuery
from typing import Optional
from package.app.api.modules.Scheduling.dto.SchedulingDto import SchedulingDto
from package.app.validation.IValidator import IValidator
from package.app.api.modules.Scheduling.SchedulingToBeFinishedValidator import SchedulingToBeFinishedValidator

class SchedulingService(metaclass=Singleton):
    def __init__(self):
        self.__SchedulingQuery = SchedulingQuery()
        self.__validator : IValidator = SchedulingToBeFinishedValidator()

    def getAll(self) -> Optional[SchedulingDto]:
        return self.__SchedulingQuery.getAll()

    def getByEmployeeId(self, employeeId:int) -> Optional[SchedulingDto]:
        return self.__SchedulingQuery.getByEmployeeId(employeeId)

    def updateJobStateID(self, schedulingKeys:str, newJobStateId: int):
        if self.__validator.execute(schedulingKeys, newJobStateId):
            employeeID, jobID, vehicleID, SchedulingDate = schedulingKeys.split(" ")
            self.__SchedulingQuery.updateJobStateID(employeeID, jobID, vehicleID, SchedulingDate, newJobStateId)
        
        #self.__SchedulingQuery.updateJobStateID(employeeId, jobID, vehicleId, date, newJobStateId)

