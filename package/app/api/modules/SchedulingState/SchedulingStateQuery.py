from typing import Optional
from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO
from package.app.api.model.SchedulingState import SchedulingState


class SchedulingStateQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()

    def getAll(self) -> Optional[SchedulingState]:
        return self.__dao.select(SchedulingState).all()

    def getSchedulingStateByDescription(self, description: str):
        return self.__dao.select(SchedulingState).where(SchedulingState.description == description).first()
