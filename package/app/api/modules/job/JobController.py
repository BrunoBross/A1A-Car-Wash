from typing import List, Optional, Set
from package.app.api.modules.job.dto.JobDto import JobDto
from package.app.decorators import post_endpoint
from package.app.meta.Singleton import Singleton
from package.app.api.modules.job.JobService import JobService


class JobController(metaclass=Singleton):
    def __init__(self):
        self.__jobService = JobService()

    def getJobs(self) -> List[JobDto]:
        return self.__jobService.getJobs()

    @post_endpoint
    def registerJob(self, job: JobDto) -> Optional[JobDto]:
        return self.__jobService.registerJob(job)

    def editJob(self, jobDto: JobDto, jobId: int):
        self.__jobService.editJob(jobDto=jobDto, jobId=jobId)

    def getJobById(self, id: int) -> Optional[JobDto]:
        return self.__jobService.getJobById(id)

    def deleteJob(self, jobId: int):
        return self.__jobService.deleteJob(jobId)
