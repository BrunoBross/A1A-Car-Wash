from sqlalchemy import Float
from package.app.api.modules.job.dto.JobDto import JobDto
from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject


class RegisterJobValidator(metaclass=Singleton):
    @validator_function
    def execute(self, jobDto: JobDto, validation: ValidationObject) -> bool:
        if not (bool(jobDto.description) and bool(jobDto.cost_value)):
            validation.errors.add("Preencha todos os campos!")
            return False
        if not isinstance(jobDto.cost_value, float):
            validation.errors.add("Insira um valor numérico para o custo!")
            return False
        return True
