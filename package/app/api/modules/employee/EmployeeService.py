from typing import Optional
from package.app.api.enum.RoleEnum import RoleEnum
from package.app.api.model.Employee import Employee
from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.api.modules.employee.EmployeeDtoMapper import EmployeeDtoMapper
from package.app.api.modules.employee.EmployeeQuery import EmployeeQuery
from package.app.api.modules.employee.dto.EmployeeDto import EmployeeDto
from package.app.api.modules.user.UserService import UserService
from package.app.api.modules.user.dto.UserDto import UserDto
from package.app.meta.Singleton import Singleton


class EmployeeService(metaclass=Singleton):
    def __init__(self):
        self.__userService = UserService()
        self.__employeeQuery = EmployeeQuery()
        self.__mapper = EmployeeDtoMapper()

    def getEmployeeByUserId(self, id: int) -> Optional[EmployeeDto]:
        employee = self.__employeeQuery.getEmployeeByUserId(id)
        if employee:
            return self.__mapper.mapEmployeeToDto(employee)

    def createEmployee(
        self, employeeDto: EmployeeDto, authDto: AuthDto
    ) -> Optional[EmployeeDto]:
        userDto = UserDto(
            username=authDto.username,
            password=authDto.password,
            role=RoleEnum.FUNCIONARIO,
        )
        self.__userService.createUser(userDto)
        userId = self.__userService.getUserByUsername(authDto.username).id
        employee = self.__employeeQuery.registerEmployee(
            Employee(
                user_id=userId,
                legal_name=employeeDto.legalName,
                wage=employeeDto.wage,
            )
        )

        if employee:
            return self.__mapper.mapEmployeeToDto(employee)
        return None
