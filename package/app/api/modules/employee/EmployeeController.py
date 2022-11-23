from typing import List, Optional, Set
from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.api.modules.employee.EmployeeService import EmployeeService
from package.app.api.modules.employee.dto.EmployeeDto import EmployeeDto
from package.app.decorators import post_endpoint
from package.app.meta.Singleton import Singleton


class EmployeeController(metaclass=Singleton):
    def __init__(self):
        self.__employeeService = EmployeeService()

    def getEmployees(self) -> List[EmployeeDto]:
        return self.__employeeService.getEmployees()

    def getEmployeeByUserId(self, id: int) -> EmployeeDto:
        return self.__employeeService.getEmployeeByUserId(id)

    @post_endpoint
    def registerEmployee(
        self, employeeDto: EmployeeDto, authDto: AuthDto
    ) -> Optional[EmployeeDto]:
        return self.__employeeService.createEmployee(
            employeeDto=employeeDto, authDto=authDto
        )

    def editEmployee(self, employeeDto: EmployeeDto, authDto: AuthDto, user_id: int):
        self.__employeeService.editEmployee(employeeDto=employeeDto, authDto=authDto, user_id=user_id)

    def deleteEmployee(self, user_id: int):
        self.__employeeService.deleteEmployee(user_id)
