from package.app.meta.Singleton import Singleton
from package.app.api.modules.SchedulingState.SchedulingStateService import SchedulingStateService
from package.app.api.modules.SchedulingState.dto.SchedulingStateDto import SchedulingStateDto

class SchedulingStateController(metaclass=Singleton):
    def __init__(self):
        self.__SchedulingStateService = SchedulingStateService()

    def getAll(self) -> SchedulingStateDto:
        return self.__SchedulingStateService.getAll()
