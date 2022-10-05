from package.app.api.modules.employee.dto.EmployeeDto import EmployeeDto
from package.app.meta.Singleton import Singleton
from package.app.api.modules.employee.EmployeeController import EmployeeController


class EmployeeComponent(metaclass=Singleton):
    def __init__(self):
        self.__employeeController = EmployeeController()

    def getEmployeeByUserId(self, id: int) -> EmployeeDto:
        return self.__employeeController.getEmployeeByUserId(id)
