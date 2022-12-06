from typing import List, Optional
from package.app.api.model.Job import Job
from package.app.exception.DatabaseIntegrityException import DatabaseIntegrityException
from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO
from package.app import sqlalchemy_session


class JobQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()
        self.__session = sqlalchemy_session

    def getJob(self, id: int) -> Optional[Job]:
        return self.__dao.get(Job, id)

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

    def getJobNyId(self, id: int) -> Optional[Job]:
        return self.__dao.select(Job).where(Job.id == id).first()

    def updateJob(self, jobUpdates: list, jobId: int):
        for update in jobUpdates:
            self.__session.query(Job).where(Job.id == jobId).update(update)
            self.__session.commit()

    def deleteJob(self, jobId: int):
        return self.__dao.delete(self.__dao.select(Job).where(Job.id == jobId).first())

    def jobAlreadyExists(self, desc: str) -> bool:
        return True if self.getJobByDescription(desc) else False

