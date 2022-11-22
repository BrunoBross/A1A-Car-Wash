from package.app.api.modules.employeeReport.employeeReportService import EmployeeReportService
from package.app.meta.Singleton import Singleton
from datetime import datetime
from package.app.api.modules.employeeReport.employeeReportValidator import EmployeeReportValidator

class EmployeeReportController(metaclass=Singleton):
    def __init__(self):
        self.__employeeReportService = EmployeeReportService()
        self.__employeeReportValidator = EmployeeReportValidator()

    def getStartMonthFormat(self, month: str):
        date = datetime.now().date()
        new_month = f'{date.year}-{month}-01'
        return new_month

    def getEndMonthFormat(self, month: str):
        date = datetime.now().date()
        new_month = f'{date.year}-{month}-31'
        return new_month

    def getEmployeeReport(self, employeeID:int, month: str):
        if self.__employeeReportValidator.execute(employeeID, month):
            startMonth = self.getStartMonthFormat(month)
            endMonth = self.getEndMonthFormat(month)
            return self.__employeeReportService.getEmployeeReport(employeeID, startMonth, endMonth)

