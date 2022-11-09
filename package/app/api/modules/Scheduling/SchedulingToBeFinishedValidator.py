from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject
from package.app.api.modules.Scheduling.dto.SchedulingDto import SchedulingDto
from package.app.api.modules.Scheduling.SchedulingQuery import SchedulingQuery



class SchedulingToBeFinishedValidator(metaclass=Singleton):
    def __init__(self) -> None:
        self.__query = SchedulingQuery()

    @validator_function
    def execute(self, schedulingInfo:list, jobStateId:int, validation: ValidationObject) -> bool:
        if not isinstance(schedulingInfo, list) or schedulingInfo == None:
            validation.errors.add("Por favor, selecione um agendamento.")
            return False
        elif not isinstance(jobStateId, str) or jobStateId == None:
            validation.errors.add("Por favor, selecione um status.")
            return False
        return True
        #vai receber o id da justificativa e os dados do agendamento
        #vai checar se sao nulos 
        #se forem da false, se nao forem da true

