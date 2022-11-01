from typing import List
from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.api.modules.employee.dto.EmployeeDto import EmployeeDto
from package.app.meta.Singleton import Singleton


class RegisterEmployeeValidator(metaclass=Singleton):
    def execute(self, employeeDto: EmployeeDto, authDto: AuthDto) -> bool:
        return (
            self.__validateNullFields(employeeDto, authDto)
            and self.__validateAuthDto(authDto)
            and self.__validateEmployeeDto(employeeDto)
        )

    def __validateEmployeeDto(self, employeeDto: EmployeeDto) -> bool:
        return self.__validateLegalName(employeeDto.legalName) and self.__validateWage(employeeDto.wage) \
               and self.__validateJobLimit(employeeDto.jobLimit)

    def __validateAuthDto(self, authDto: AuthDto) -> bool:
        return self.__validateUsername(authDto.username) and self.__validatePassword(
            authDto.password
        )

    def __validateNullFields(self, employeeDto: EmployeeDto, authDto: AuthDto):
        if not (
            bool(authDto.username)
            and bool(authDto.password)
            and bool(employeeDto.legalName)
            and bool(employeeDto.wage)
        ):
            print("\033[1;91m Preencha todos os campos!")
            return False
        return True

    def __validatePassword(self, password: str):
        if len(password) < 8 or len(password) > 255:
            print(
                "\033[1;91m Uma senha deve possuir no mínimo 8 e no máximo 255 caracteres \033[0m"
            )
            return False
        return True

    def __validateUsername(self, username: str):
        if len(username) < 5:
            print("\033[1;91m Digite um username com pelo menos 5 caracteres \033[0m")
            return False
        if " " in username:
            print("\033[1;91m Não deve conter espaço no nome de usuário \033[0m")
            return False
        return True

    def __validateWage(self, salary: str):
        if not salary.isnumeric():
            print("\033[1;91m Digite um valor inteiro para o salário \033[0m")
            return False
        elif int(salary) < 1200:
            print("\033[1;91m Digite um salário maior que 1200 \033[0m")
            return False
        return True

    def __validateLegalName(self, fullname: str):
        name_split: List = fullname.split(" ")
        for name in name_split:
            if len(name) < 2:
                print("\033[1;91m Cada nome deve ter pelo menos 2 caracteres \033[0m")
                return False
        if len(name_split) < 2:
            print("\033[1;91m Digite um nome completo \033[0m")
            return False
        return True

    def __validateJobLimit(self, job_limit: str):
        print("ENTROU")
        if not job_limit.isnumeric():
            print("\033[1;91m Digite um valor inteiro para o limite de serviços \033[0m")
            return False
        elif int(job_limit) > 10 or int(job_limit) < 5:
            print("\033[1;91m O limite de serviços deve ser entre 5 e 10 serviços \033[0m")
            return False
        return True
