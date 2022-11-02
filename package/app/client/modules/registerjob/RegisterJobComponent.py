from package.app.api.modules.job.JobController import JobController
from package.app.client.modules.registerjob.RegisterJobValidator import (
    RegisterJobValidator,
)
from package.app.client.state.ComponentState import ComponentState
from package.app.meta.Singleton import Singleton
from package.app.client.utils.form import getEntryBuffer
from package.app.api.modules.job.dto.JobDto import JobDto


class RegisterJobComponent(metaclass=Singleton):
    def __init__(self):
        self.__state = ComponentState()
        self.__validator = RegisterJobValidator()
        self.__controller = JobController()

    def requestRegistration(self):

        description = getEntryBuffer(self.__state.getReferenceById("jobName"))
        cost_value = getEntryBuffer(self.__state.getReferenceById("jobValue"))

        dto = JobDto(
            description=description,
            cost_value=float((cost_value) if bool(cost_value) else 0),
        )

        if self.__validator.execute(dto):
            self.__controller.registerJob(dto)

    def getState(self) -> ComponentState:
        return self.__state
