from package.app.api.modules.employee.dto.EmployeeDto import EmployeeDto
from package.app.client.state.UserContext import UserContext
from package.app.meta.Singleton import Singleton
from package.app.api.modules.employee.EmployeeController import EmployeeController


class EmployeeComponent(metaclass=Singleton):
    def __init__(self):
        self.__employeeController = EmployeeController()
        self.__userContext = UserContext()

    def getEmployeeByUserId(self, id: int) -> EmployeeDto:
        return self.__employeeController.getEmployeeByUserId(id)

    def getUserContext(self) -> UserContext:
        return self.__userContext
