from package.app.meta.Singleton import Singleton
from package.app.api.modules.SchedulingState.SchedulingStateQuery import SchedulingStateQuery
from typing import Optional
from package.app.api.modules.SchedulingState.dto.SchedulingStateDto import SchedulingStateDto

class SchedulingStateService(metaclass=Singleton):
    def __init__(self):
        self.__SchedulingStateQuery = SchedulingStateQuery()

    def getAll(self) -> Optional[SchedulingStateDto]:
        return self.__SchedulingStateQuery.getAll()

    def getSchedulingStateByDescription(self, description: str):
        return self.__SchedulingStateQuery.getSchedulingStateByDescription(description)

