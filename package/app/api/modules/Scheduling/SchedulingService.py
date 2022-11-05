from package.app.meta.Singleton import Singleton
from package.app.api.modules.Scheduling.SchedulingQuery import SchedulingQuery
from typing import Optional
from package.app.api.modules.Scheduling.dto.SchedulingDto import SchedulingDto

class SchedulingService(metaclass=Singleton):
    def __init__(self):
        self.__SchedulingQuery = SchedulingQuery()

    def getAll(self) -> Optional[SchedulingDto]:
        return self.__SchedulingQuery.getAll()

