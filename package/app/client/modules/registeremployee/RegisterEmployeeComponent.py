from package.app.meta.Singleton import Singleton
from package.app.api.modules.user.UserService import UserService
from package.app.api.modules.employee.EmployeeController import EmployeeController
from package.app.client.state.ComponentState import ComponentState
from package.app.client.utils.form import getEntryBuffer


class RegisterEmployeeComponent(metaclass=Singleton):
    def __init__(self):
        self.__userService = UserService()
        self.__employeeController = EmployeeController()
        self.__state = ComponentState()

    def registerEmployee(self):
        username = getEntryBuffer(self.__state.getReferenceById("username"))
        fullname = getEntryBuffer(self.__state.getReferenceById("fullname"))
        password = getEntryBuffer(self.__state.getReferenceById("password"))
        salary = getEntryBuffer(self.__state.getReferenceById("salary"))

        self.__employeeController.registerEmployee(username, fullname, password, salary)

    def getState(self) -> ComponentState:
        return self.__state
