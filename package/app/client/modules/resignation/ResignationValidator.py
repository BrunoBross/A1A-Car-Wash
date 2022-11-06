from sqlalchemy import Float
from package.app.api.modules.resignation.dto.ResignationDto import ResignationDto
from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject


class ResignationValidator(metaclass=Singleton):
    
    # NEED FIXING
    @validator_function
    def execute(self, resignationDto: ResignationDto, validation: ValidationObject) -> bool:
        if not (bool(resignationDto.description) and bool(resignationDto.cost_value)):
            validation.errors.add("Preencha todos os campos!")
            return False
        if not isinstance(resignationDto.cost_value, float):
            validation.errors.add("Insira um valor numérico para o custo!")
            return False
        return True
