from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject
from package.app.api.modules.Scheduling.dto.SchedulingDto import SchedulingDto
from package.app.api.modules.Scheduling.SchedulingQuery import SchedulingQuery



class SchedulingValidator(metaclass=Singleton):
    def __init__(self) -> None:
        self.__query = SchedulingQuery()

    @validator_function
    def ValidateAgendamento(self, SchedulingDto: SchedulingDto, userEmployeeId: int) -> bool:
        if SchedulingDto.employee_id == userEmployeeId and SchedulingDto.job_state_id == 1:
            return True
        return False
        
