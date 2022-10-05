from typing import Optional
from package.app.api.modules.job.JobDtoMapper import JobDtoMapper
from package.app.api.modules.job.dto.JobDto import JobDto
from package.app.meta.Singleton import Singleton
from package.app.api.modules.job.JobQuery import JobQuery


class JobService(metaclass=Singleton):
    def __init__(self):
        self.__query = JobQuery()
        self.__mapper = JobDtoMapper()

    def registerJob(self, jobDto: JobDto) -> Optional[JobDto]:
        if self.__query.registerJob(self.__mapper.mapDtoToJob(jobDto)):
            return jobDto
        return None
