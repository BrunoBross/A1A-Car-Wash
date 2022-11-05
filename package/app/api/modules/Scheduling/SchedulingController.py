from package.app.meta.Singleton import Singleton
from package.app.api.modules.Scheduling.SchedulingService import SchedulingService
from package.app.api.modules.Scheduling.dto.SchedulingDto import SchedulingDto

class SchedulingController(metaclass=Singleton):
    def __init__(self):
        self.__SchedulingService = SchedulingService()

    def getAll(self) -> SchedulingDto:
        return self.__SchedulingService.getAll()
