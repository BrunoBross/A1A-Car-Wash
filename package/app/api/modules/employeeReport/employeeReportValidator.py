from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject
from package.app.api.modules.Scheduling.dto.SchedulingDto import SchedulingDto
from package.app.api.modules.Scheduling.SchedulingQuery import SchedulingQuery



class EmployeeReportValidator(metaclass=Singleton):
    def __init__(self) -> None:
        self.__query = SchedulingQuery()

    @validator_function
    def execute(self, employeeID: int, month:str, validation: ValidationObject) -> bool:
        if not isinstance(employeeID, int) or employeeID == None or employeeID == 0:
            validation.errors.add("Por favor, selecione um funcionario")
            return False
        elif not isinstance(month, str) or month == None or month == "":
            validation.errors.add("Por favor, selecione um mês.")
            return False
        return True
        #vai receber o id da justificativa e os dados do agendamento
        #vai checar se sao nulos 
        #se forem da false, se nao forem da true

