from package.app.api.modules.billing.BillingService import BillingService
from package.app.meta.Singleton import Singleton
from datetime import datetime


class BillingController(metaclass=Singleton):
    def __init__(self):
        self.__billingService = BillingService()

    def getBilling(self, start_date: str, end_date: str):
        return self.__billingService.getBilling(start_date, end_date)

    def getStartMonthFormat(self, month: str):
        date = datetime.now().date()
        new_month = f'{date.year}-{month}-01'
        return new_month

    def getEndMonthFormat(self, month: str):
        date = datetime.now().date()
        new_month = f'{date.year}-{month}-31'
        return new_month
