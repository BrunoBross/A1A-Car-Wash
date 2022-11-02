from package.app.api.modules.job.dto.JobDto import JobDto
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject
from package.app.validation.ValidationService import ValidationService


class RegisterJobValidator(metaclass=Singleton):
    def __init__(self):
        self.__validationService = ValidationService()

    def execute(self, jobDto: JobDto) -> bool:
        if not (bool(jobDto.description) and bool(jobDto.cost_value)):
            validation = ValidationObject(field="*")
            validation.errors.add("Preencha todos os campos!")
            self.__validationService.post(validation)
            return False
        return True
