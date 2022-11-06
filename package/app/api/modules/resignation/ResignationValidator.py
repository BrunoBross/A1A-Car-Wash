from package.app.api.modules.resignation.dto.ResignationDto import ResignationDto
from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.api.modules.resignation.ResignationQuery import ResignationQuery
from package.app.validation.ValidationObject import ValidationObject


class ResignationValidator(metaclass=Singleton):
    def __init__(self):
        self.__query = ResignationQuery()

    # NEED FIXING
    @validator_function
    def execute(self, resignationDto: ResignationDto, validation: ValidationObject) -> bool:
        if self.__query.getResignationByDescription(resignationDto.description):
            validation.errors.add(
                f"Serviço '{resignationDto.description}' já cadastrado. Por favor tente um valor diferente."
            )
            return False
        return True
