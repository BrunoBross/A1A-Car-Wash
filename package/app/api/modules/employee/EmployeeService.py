from typing import List, Optional, Set
from package.app.api.enum.RoleEnum import RoleEnum
from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.api.modules.employee.EmployeeDtoMapper import EmployeeDtoMapper
from package.app.api.modules.employee.EmployeeQuery import EmployeeQuery
from package.app.api.modules.employee.EmployeeValidator import EmployeeValidator
from package.app.api.modules.employee.dto.EmployeeDto import EmployeeDto
from package.app.api.modules.user.UserService import UserService
from package.app.api.modules.user.dto.UserDto import UserDto
from package.app.meta.Singleton import Singleton
from package.app.validation.IValidator import IValidator


class EmployeeService(metaclass=Singleton):
    def __init__(self):
        self.__userService = UserService()
        self.__employeeQuery = EmployeeQuery()
        self.__mapper = EmployeeDtoMapper()
        self.__validator: IValidator = EmployeeValidator()

    def getEmployees(self) -> List[EmployeeDto]:
        result = list()
        for employee in self.__employeeQuery.getEmployees():
            result.append(self.__mapper.mapEmployeeToDto(employee))
        return result

    def getEmployeeByUserId(self, id: int) -> Optional[EmployeeDto]:
        employee = self.__employeeQuery.getEmployeeByUserId(id)
        if employee:
            return self.__mapper.mapEmployeeToDto(employee)

    def createEmployee(
        self, employeeDto: EmployeeDto, authDto: AuthDto
    ) -> Optional[EmployeeDto]:
        if not self.__validator.execute(authDto):
            return None
        userDto = UserDto(
            username=authDto.username,
            password=authDto.password,
            role=RoleEnum.FUNCIONARIO,
        )
        self.__userService.createUser(userDto)

        userId = self.__userService.getUserByUsername(authDto.username).id
        employeeDto.user = UserDto(id=userId)

        employee = self.__employeeQuery.registerEmployee(
            self.__mapper.mapDtoToEmployee(employeeDto)
        )

        return self.__mapper.mapEmployeeToDto(employee)
