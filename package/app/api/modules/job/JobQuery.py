from typing import List, Optional
from package.app.api.model.Job import Job
from package.app.exception.DatabaseIntegrityException import DatabaseIntegrityException
from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO


class JobQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()

    def getJobs(self) -> List[Job]:
        return self.__dao.select(Job).all()

    def registerJob(self, job: Job) -> Optional[Job]:
        try:
            self.__dao.insert(job)
            return job
        except DatabaseIntegrityException:
            return None

    def getJobByDescription(self, description: str) -> Optional[Job]:
        return self.__dao.select(Job).where(Job.description == description).first()
