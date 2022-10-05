from typing import Optional
from package.app.api.modules.employee.EmployeeQuery import EmployeeQuery
from package.app.api.modules.user.UserQuery import UserQuery
from package.app.api.modules.user.dto.EmployeeDto import EmployeeDto
from package.app.meta.Singleton import Singleton


class EmployeeService(metaclass=Singleton):
    def __init__(self):
        self.__employeeQuery = EmployeeQuery()
        self.__userQuery = UserQuery()

    def getEmployeeFullNameByUsername(self, username: str) -> Optional[EmployeeDto]:
        user = self.__userQuery.getUserByUsername(username)
        employee = self.__employeeQuery.getEmployeeById(user.id)
        if employee:
            return employee.legal_name
        return None

    def registerEmployee(self, username: str, fullname: str, password: str, salary: str):
        self.__employeeQuery.registerEmployee(username, fullname, password, salary)

