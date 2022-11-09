from typing import Optional
from package.app.api.modules.scheduling.SchedulingService import SchedulingService
from package.app.api.modules.scheduling.dto.SchedulingDto import SchedulingDto
from package.app.decorators import post_endpoint
from package.app.meta.Singleton import Singleton


class SchedulingController(metaclass=Singleton):
    def __init__(self):
        self.__schedulingService = SchedulingService()

    @post_endpoint
    def registerScheduling(
        self, schedulingDto: SchedulingDto
    ) -> Optional[SchedulingDto]:
        return self.__schedulingService.registerScheduling(schedulingDto)
