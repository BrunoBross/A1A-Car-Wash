from typing import Optional
from package.app.api.modules.scheduling.SchedulingQuery import SchedulingQuery
from package.app.api.modules.scheduling.dto.SchedulingDto import SchedulingDto
from package.app.meta.Singleton import Singleton


class SchedulingService(metaclass=Singleton):
    def __init__(self):
        self.__query = SchedulingQuery()

    def registerScheduling(
        self, schedulingDto: SchedulingDto
    ) -> Optional[SchedulingDto]:
        pass
