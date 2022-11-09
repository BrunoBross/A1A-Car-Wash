from datetime import datetime
from package.app.api.modules.scheduling.dto.SchedulingDto import SchedulingDto
from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject


class SchedulingValidator(metaclass=Singleton):
    @validator_function
    def execute(self, dto: SchedulingDto, validation: ValidationObject) -> bool:
        return self.__validateAllFieldsFilled(
            dto, validation
        ) and self.__validateDateNotPast(dto, validation)

    def __validateAllFieldsFilled(
        self, dto: SchedulingDto, validation: ValidationObject
    ) -> bool:
        if not bool(
            dto.date
            and dto.employee.id != -1
            and dto.vehicle.id != -1
            and dto.job.id != -1
        ):
            validation.errors.add("Preencha todos os campos!")
            return False
        return True

    def __validateDateNotPast(
        self, dto: SchedulingDto, validation: ValidationObject
    ) -> bool:
        if dto.date < datetime.now().date():
            validation.errors.add("Data selecionada deve ser posterior a data atual!")
            return False
        return True
