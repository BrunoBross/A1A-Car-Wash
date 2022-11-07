from package.app.api.modules.billing.BillingService import BillingService
from package.app.meta.Singleton import Singleton
from datetime import datetime


class BillingController(metaclass=Singleton):
    def __init__(self):
        self.__billingService = BillingService()

    def getGrossRevenue(self, start_date: str, end_date: str):
        return self.__billingService.getGrossRevenue(start_date, end_date)

    def getNetRevenue(self, start_date: str, end_date: str):
        return self.__billingService.getNetRevenue(start_date, end_date)

    def getEmployeeWages(self, start_date: str, end_date: str):
        return self.__billingService.getEmployeeWages(start_date, end_date)

    def getTaxes(self, start_date: str, end_date: str):
        return self.__billingService.getTaxes(start_date, end_date)

    def getStartMonthFormat(self, month: str):
        date = datetime.now().date()
        new_month = f'{date.year}-{month}-01'
        return new_month

    def getEndMonthFormat(self, month: str):
        date = datetime.now().date()
        new_month = f'{date.year}-{month}-31'
        return new_month
