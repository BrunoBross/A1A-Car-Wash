from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.api.modules.employee.dto.EmployeeDto import EmployeeDto
from package.app.api.modules.user.UserQuery import UserQuery
from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject


class EmployeeValidator(metaclass=Singleton):
    def __init__(self):
        self.__query = UserQuery()

    @validator_function
    def execute(self, authDto: AuthDto, validation: ValidationObject) -> bool:
        print(authDto)
        if self.__query.getUserByUsername(authDto.username):
            validation.errors.add(
                f"Usuário '{authDto.username}' já cadastrado. Por favor tente um valor diferente."
            )
            return False
        return True
