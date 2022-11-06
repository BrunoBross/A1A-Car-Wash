from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject
from package.app.api.modules.Scheduling.dto.SchedulingDto import SchedulingDto
from package.app.api.modules.Scheduling.SchedulingQuery import SchedulingQuery



class SchedulingValidator(metaclass=Singleton):
    def __init__(self) -> None:
        self.__query = SchedulingQuery()

    @validator_function
    def ValidadeSchedulingToBeFinished(self, schedulingKeys:str, schedulingStateId:int, validation: ValidationObject) -> bool:
        if schedulingKeys == None or schedulingStateId == None:
            validation.errors.add("Por favor, selecione um agendamento ou uma situação")
            return False
        return True
        #vai receber o id da justificativa e os dados do agendamento
        #vai checar se sao nulos 
        #se forem da false, se nao forem da true

