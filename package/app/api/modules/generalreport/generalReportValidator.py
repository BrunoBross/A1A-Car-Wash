from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject
from package.app.api.modules.Scheduling.dto.SchedulingDto import SchedulingDto
from package.app.api.modules.Scheduling.SchedulingQuery import SchedulingQuery



class GeneralReportValidator(metaclass=Singleton):
    def __init__(self) -> None:
        self.__query = SchedulingQuery()

    @validator_function
    def execute(self, employeeID: int, month:str, validation: ValidationObject) -> bool:
        return True