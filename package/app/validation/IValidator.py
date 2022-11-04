from typing import Any, Callable, Protocol

from package.app.decorators import validator_function
from package.app.validation.ValidationObject import ValidationObject


class IValidator(Protocol):
    @validator_function
    def execute(self, validation: ValidationObject, *args, **kwargs) -> bool:
        ...
