from package.app.api.modules.warning.dto.WarningDto import WarningDto
from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject


class RegisterWarningValidator(metaclass=Singleton):
    @validator_function
    def execute(
        self, warningDto: WarningDto, validation: ValidationObject, *args, **kwargs
    ) -> bool:
        if not bool(warningDto.description):
            validation.errors.add(f"Preenchimento obrigatório dos campos.")
            return False
        return True
