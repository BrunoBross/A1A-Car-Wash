from typing import List, Optional, Set
from package.app.api.modules.job.JobDtoMapper import JobDtoMapper
from package.app.api.modules.job.JobValidator import JobValidator
from package.app.api.modules.job.dto.JobDto import JobDto
from package.app.meta.Singleton import Singleton
from package.app.api.modules.job.JobQuery import JobQuery
from package.app.validation.IValidator import IValidator
from package.app.api.modules.scheduling.SchedulingQuery import SchedulingQuery


class JobService(metaclass=Singleton):
    def __init__(self):
        self.__query = JobQuery()
        self.__mapper = JobDtoMapper()
        self.__validator: IValidator = JobValidator()
        self.__schedulingQuery = SchedulingQuery()

    def getJobs(self) -> List[JobDto]:
        result = list()
        for job in self.__query.getJobs():
            result.append(self.__mapper.mapJobToDto(job))
        return result

    def registerJob(self, jobDto: JobDto) -> Optional[JobDto]:
        if self.__validator.execute(jobDto):
            self.__query.registerJob(self.__mapper.mapDtoToJob(jobDto))
            return jobDto
        return None

    def editJob(self, jobDto: JobDto, jobId: int):
        jobUpdates = []
        if jobDto.description != "":
            jobUpdates.append({"description": jobDto.description})
        if jobDto.cost_value != "":
            jobUpdates.append({"cost_value": jobDto.cost_value})
        if len(jobUpdates) > 0:
            self.__query.updateJob(jobUpdates, jobId)

    def getJobById(self, id:int) -> Optional[JobDto]:
        return self.__query.getJobNyId(id)

    def getJobByDescription(self, description: str):
        return self.__query.getJobByDescription(description)

    def deleteJob(self, jobId: int):
        if len(self.__schedulingQuery.getSchedulingsByJobId(jobId)) > 0:
            return False
        self.__query.deleteJob(jobId)
        return True
