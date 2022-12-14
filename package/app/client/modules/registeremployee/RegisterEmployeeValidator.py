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
        self, employeeDto: EmployeeDto, authDto: AuthDto, isEdit: bool, validation: ValidationObject
    ) -> bool:
        return (
            self.__validateNullFields(employeeDto, authDto, isEdit, validation)
            and self.__validateAuthDto(authDto, isEdit, validation)
            and self.__validateEmployeeDto(employeeDto, isEdit, validation)
        )

    def __validateEmployeeDto(
        self, employeeDto: EmployeeDto, isEdit: bool, validation: ValidationObject
    ) -> bool:
        return (
            self.__validateLegalName(employeeDto.legalName, isEdit, validation)
            and self.__validateWage(employeeDto.wage, isEdit, validation)
            and self.__validateJobLimit(employeeDto.jobLimit, isEdit, validation)
        )

    def __validateAuthDto(self, authDto: AuthDto, isEdit: bool, validation: ValidationObject) -> bool:
        return self.__validateUsername(
            authDto.username, isEdit, validation
        ) and self.__validatePassword(authDto.password, isEdit, validation)

    def __validateNullFields(
        self, employeeDto: EmployeeDto, authDto: AuthDto, isEdit: bool, validation=ValidationObject
    ):
        if isEdit:
            if not(
                bool(authDto.username)
                or bool(authDto.password)
                or bool(employeeDto.legalName)
                or bool(employeeDto.wage)
            ):
                validation.errors.add("Preencha pelo menos um campo!")
                return False
            return True
        if not (
            bool(authDto.username)
            and bool(authDto.password)
            and bool(employeeDto.legalName)
            and bool(employeeDto.wage)
        ):
            validation.errors.add("Preencha todos os campos!")
            return False
        return True

    def __validateWage(self, salary: str, isEdit: bool, validation: ValidationObject):
        if salary == "" and isEdit:
            return True
        if not salary.isnumeric():
            validation.errors.add("Digite um valor inteiro para o sal??rio")
            return False
        elif int(salary) < 1200:
            validation.errors.add(
                f"Digite um sal??rio maior que {Config.EMPLOYEE_WAGE_DEFAULT}"
            )
            return False
        return True

    def __validatePassword(self, password: str, isEdit: bool, validation: ValidationObject):
        if password == "" and isEdit:
            return True
        if len(password) < 8 or len(password) > 255:
            validation.errors.add(
                "Uma senha deve possuir no m??nimo 8 e no m??ximo 255 caracteres"
            )
            return False
        return True

    def __validateUsername(self, username: str, isEdit: bool, validation: ValidationObject):
        if username == "" and isEdit:
            return True
        if len(username) < 5:
            validation.errors.add("Digite um username com pelo menos 5 caracteres")
            return False
        if " " in username:
            validation.errors.add("N??o deve conter espa??o no nome de usu??rio")
            return False
        return True

    def __validateLegalName(self, fullname: str, isEdit: bool, validation: ValidationObject):
        if fullname == "" and isEdit:
            return True

        name_split: List = fullname.split(" ")
        for name in name_split:
            if len(name) < 2:
                validation.errors.add("Cada nome deve ter pelo menos 2 caracteres")
                return False
        if len(name_split) < 2:
            validation.errors.add("Digite um nome completo")
            return False
        return True

    def __validateJobLimit(self, job_limit: str, isEdit: bool, validation: ValidationObject):
        if job_limit == "" and isEdit:
            return True
        if not job_limit.isnumeric():
            validation.errors.add("Digite um valor inteiro para o limite de servi??os.")
            return False
        if not (5 <= int(job_limit) <= 10):
            validation.errors.add(
                f"O limite de servi??os deve ser entre {Config.EMPLOYEE_MIN_JOBS_DEFAULT} e {Config.EMPLOYEE_MAX_JOBS_DEFAULT} servi??os."
            )
            return False
        return True
