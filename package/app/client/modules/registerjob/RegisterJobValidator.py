from sqlalchemy import Float
from package.app.api.modules.job.dto.JobDto import JobDto
from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject


class RegisterJobValidator(metaclass=Singleton):
    @validator_function
    def execute(self, jobDto: JobDto, isEdit: bool, already_exists: bool, validation: ValidationObject) -> bool:
        if isEdit:
            if not(
                bool(jobDto.cost_value)
                or bool(jobDto.description)
            ):
                validation.errors.add("Preencha pelo menos um campo!")
                return False
            if already_exists:
                validation.errors.add(
                    "Já existe um serviço com este nome! Escolha outro nome ou altere o nome do serviço já existente.")
                return False
        if not (bool(jobDto.description) and bool(jobDto.cost_value) and not isEdit):
            validation.errors.add("Preencha todos os campos!")
            return False
        if not isinstance(jobDto.cost_value, float):
            validation.errors.add("Insira um valor numérico para o custo!")
            return False
        return True
