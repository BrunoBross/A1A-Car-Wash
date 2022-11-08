from typing import Optional
from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.api.modules.employee.EmployeeService import EmployeeService
from package.app.api.modules.employee.dto.EmployeeDto import EmployeeDto
from package.app.meta.Singleton import Singleton


class EmployeeController(metaclass=Singleton):
    def __init__(self):
        self.__employeeService = EmployeeService()

    def getEmployeeById(self, id: int) -> EmployeeDto:
        return self.__employeeService.getEmployeeById(id)

    def registerEmployee(
        self, employeeDto: EmployeeDto, authDto: AuthDto
    ) -> Optional[EmployeeDto]:
        return self.__employeeService.createEmployee(
            employeeDto=employeeDto, authDto=authDto
        )
