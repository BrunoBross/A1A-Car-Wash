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

    def getAllByEmployeeId(self, employeeID: int) -> Optional[SchedulingDto]:
        return self.__SchedulingQuery.getAllByEmployeeID(employeeID)

    def updateJobStateID(self, employeeId: int, jobId: int, vehicleId: int, date: str, newJobStateId: int):
        self.__SchedulingQuery.updateJobStateID(employeeId, jobId, vehicleId, date, newJobStateId)

    def getSchedulingByEmployeeIDAndDate(self, employeeID:int, startMonth:str, endMonth:str) -> Optional[SchedulingDto]:
        return self.__SchedulingQuery.getSchedulingByEmployeeIDAndDate(employeeID, startMonth, endMonth)