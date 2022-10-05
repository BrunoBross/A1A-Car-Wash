from package.app.meta.Singleton import Singleton
from package.app.api.modules.employee.EmployeeController import EmployeeController


class EmployeeComponent(metaclass=Singleton):
    def __init__(self):
        self.__employeeController = EmployeeController()

    def getEmployeeFullNameByUsername(self, username: str):
        return self.__employeeController.getEmployeeFullNameByUsername(username)
