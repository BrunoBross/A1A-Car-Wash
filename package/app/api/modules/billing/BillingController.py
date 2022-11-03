from package.app.api.modules.billing.BillingService import BillingService
from package.app.meta.Singleton import Singleton


class BillingController(metaclass=Singleton):
    def __init__(self):
        self.__billingService = BillingService()

    def getGrossRevenue(self, month: str):
        return self.__billingService.getGrossRevenue(month)

    def getNetRevenue(self, month: str):
        return self.__billingService.getNetRevenue(month)

    def getEmployeeWages(self, month: str):
        return self.__billingService.getEmployeeWages(month)

    def getTaxes(self, month: str):
        return self.__billingService.getTaxes(month)
