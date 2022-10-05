from package.app.api.modules.employee.EmployeeService import EmployeeService
from package.app.meta.Singleton import Singleton


class EmployeeController(metaclass=Singleton):
    def __init__(self):
        self.__employeeService = EmployeeService()

    def registerEmployee(self, username: str, fullname: str, password: str, salary: str):
        self.__employeeService.registerEmployee(username, fullname, password, salary)

    def getEmployeeFullNameByUsername(self, username: str):
        return self.__employeeService.getEmployeeFullNameByUsername(username)
