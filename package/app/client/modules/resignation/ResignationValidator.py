from sqlalchemy import Float
from package.app.api.modules.resignation.dto.ResignationDto import ResignationDto
from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject


class ResignationValidator(metaclass=Singleton):
    
    @validator_function
    def execute(self, resignationDto: ResignationDto, validation: ValidationObject) -> bool:
        if not (bool(resignationDto.employee and resignationDto.resignation_type)):
            validation.errors.add("Selecione um funcionário e um tipo de causa!")
            return False
        if len(resignationDto.memo) > 255:
            validation.errors.add("A observação excede o tamanho limite de 255 caracteres!")
            return False
        return True
