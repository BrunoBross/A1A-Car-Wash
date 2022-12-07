from package.app.api.modules.generalreport.generalReportService import GeneralReportService
from package.app.meta.Singleton import Singleton
from datetime import datetime

class GeneralReportController(metaclass=Singleton):
    def __init__(self):
        self.__generalReportService = GeneralReportService()

    def getStartMonthFormat(self, month: str):
        date = datetime.now().date()
        new_month = f'{date.year}-{month}-01'
        return new_month

    def getEndMonthFormat(self, month: str):
        date = datetime.now().date()
        new_month = f'{date.year}-{month}-31'
        return new_month

    def getGeneralReport(self, month: str):
        startMonth = self.getStartMonthFormat(month)
        endMonth = self.getEndMonthFormat(month)
        return self.__generalReportService.getGeneralReport(startMonth, endMonth)