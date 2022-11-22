from typing import Optional
from package.app.api.modules.job.JobService import JobService
from package.app.api.modules.scheduling.SchedulingDtoMapper import SchedulingDtoMapper
from package.app.api.modules.scheduling.SchedulingQuery import SchedulingQuery
from package.app.api.modules.scheduling.SchedulingValidator import SchedulingValidator
from package.app.api.modules.scheduling.dto.SchedulingDto import SchedulingDto
from package.app.meta.Singleton import Singleton
from package.app.validation.IValidator import IValidator


class SchedulingService(metaclass=Singleton):
    def __init__(self):
        self.__schedulingQuery = SchedulingQuery()
        self.__jobService = JobService()
        self.__validator: IValidator = SchedulingValidator()
        self.__mapper = SchedulingDtoMapper()

    def registerScheduling(
        self, schedulingDto: SchedulingDto
    ) -> Optional[SchedulingDto]:
        if not self.__validator.execute(schedulingDto):
            return None
        self.__schedulingQuery.createScheduling(
            self.__mapper.mapDtoToScheduling(schedulingDto)
        )
        return schedulingDto

    def getSchedulingByEmployeeIDAndDate(self, employeeID:int, startMonth:str, endMonth:str) -> Optional[SchedulingDto]:
        return self.__schedulingQuery.getSchedulingByEmployeeIDAndDate(employeeID, startMonth, endMonth)