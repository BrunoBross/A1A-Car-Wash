from package.app.api.modules.employee.EmployeeController import EmployeeController
from package.app.meta.Singleton import Singleton
from package.app.api.modules.billing.BillingController import BillingController
from package.app.api.modules.employeeReport.employeeReportController import EmployeeReportController

class EmployeeReportComponent(metaclass=Singleton):
    def __init__(self):
        self.__employeeController = EmployeeController()
        self.__billingController = BillingController()
        self.__employeeReportController = EmployeeReportController()
        

    def getEmployees(self):
        return self.__employeeController.getEmployees()

    def getStartMonthFormat(self, month):
        return self.__employeeReportController.getStartMonthFormat(month)

    def getEmployeeReport(self, employeeID:int, month:str):
        return self.__employeeReportController.getEmployeeReport(employeeID, month)
