from typing import List
from package.Config import Config
from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.api.modules.employee.dto.EmployeeDto import EmployeeDto
from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject


class RegisterEmployeeValidator(metaclass=Singleton):
    @validator_function
    def execute(
        self, employeeDto: EmployeeDto, authDto: AuthDto, validation: ValidationObject
    ) -> bool:
        return (
            self.__validateNullFields(employeeDto, authDto, validation)
            and self.__validateAuthDto(authDto, validation)
            and self.__validateEmployeeDto(employeeDto, validation)
        )

    def __validateEmployeeDto(
        self, employeeDto: EmployeeDto, validation: ValidationObject
    ) -> bool:
        return self.__validateLegalName(
            employeeDto.legalName, validation
        ) and self.__validateWage(employeeDto.wage, validation)

    def __validateAuthDto(self, authDto: AuthDto, validation: ValidationObject) -> bool:
        return self.__validateUsername(
            authDto.username, validation
        ) and self.__validatePassword(authDto.password, validation)

    def __validateNullFields(
        self, employeeDto: EmployeeDto, authDto: AuthDto, validation=ValidationObject
    ):
        if not (
            bool(authDto.username)
            and bool(authDto.password)
            and bool(employeeDto.legalName)
            and bool(employeeDto.wage)
        ):
            validation.errors.add("Preencha todos os campos!")
            return False
        return True

    def __validateWage(self, salary: str, validation: ValidationObject):
        if not salary.isnumeric():
            validation.errors.add("Digite um valor inteiro para o salário")
            return False
        elif int(salary) < 1200:
            validation.errors.add(
                f"Digite um salário maior que {Config.EMPLOYEE_WAGE_DEFAULT}"
            )
            return False
        return True

    def __validatePassword(self, password: str, validation: ValidationObject):
        if len(password) < 8 or len(password) > 255:
            validation.errors.add(
                "Uma senha deve possuir no mínimo 8 e no máximo 255 caracteres"
            )
            return False
        return True

    def __validateUsername(self, username: str, validation: ValidationObject):
        if len(username) < 5:
            validation.errors.add("Digite um username com pelo menos 5 caracteres")
            return False
        if " " in username:
            validation.errors.add("Não deve conter espaço no nome de usuário")
            return False
        return True

    def __validateLegalName(self, fullname: str, validation: ValidationObject):
        name_split: List = fullname.split(" ")
        for name in name_split:
            if len(name) < 2:
                validation.errors.add("Cada nome deve ter pelo menos 2 caracteres")
                return False
        if len(name_split) < 2:
            validation.errors.add("Digite um nome completo")
            return False
        return True
