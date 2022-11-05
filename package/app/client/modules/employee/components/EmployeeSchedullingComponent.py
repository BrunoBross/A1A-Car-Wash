from package.app.meta.Singleton import Singleton
from package.app.api.modules.SchedulingState.SchedulingStateController import SchedulingStateController
from package.app.api.modules.Scheduling.SchedulingController import SchedulingController
from package.app.client.state.ComponentState import ComponentState
from package.app.api.modules.SchedulingState.dto.SchedulingStateDto import SchedulingStateDto
from package.app.api.modules.Scheduling.dto.SchedulingDto import SchedulingDto


class EmployeeSchedulingComponent(metaclass=Singleton):

    def __init__(self):
        self.__SchedulingStateController = SchedulingStateController()
        self.__SchedulingController = SchedulingController()
        self.__state = ComponentState()

    #esse cara faz a logica
    #Seleciona o cara na lista
    #Seleciona o estado dele

    def getAllSchedulingStates(self) -> SchedulingStateDto:
        return self.__SchedulingStateController.getAll()

    def getAllScheduling(self) -> SchedulingDto:
        return self.__SchedulingController.getAll()