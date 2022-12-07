from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject


class RegisterWarningValidator(metaclass=Singleton):
    def execute(self, validation: ValidationObject, *args, **kwargs) -> bool:
        return True
