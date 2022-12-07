from sqlalchemy import Float
from package.app.api.modules.resignation.dto.ResignationDto import ResignationDto
from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject


class GeneralReportValidator(metaclass=Singleton):

    @validator_function
    def execute(self, month: str, validation: ValidationObject) -> bool:
        if month == "":
            validation.errors.add("Por favor, selecione um mês.")
            return False
        return True
