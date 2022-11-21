from package.app.api.modules.employee.EmployeeController import EmployeeController
from package.app.meta.Singleton import Singleton


class EmployeeReportComponent(metaclass=Singleton):
    def __init__(self):
        self.__employeeController = EmployeeController()
        

    def getText(self) -> str:
        return self.__exemploController.getExampleInfo()

    def getEmployees(self):
        return self.__employeeController.getEmployees()