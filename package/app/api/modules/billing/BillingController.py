from package.app.api.modules.billing.BillingService import BillingService
from package.app.meta.Singleton import Singleton


class BillingController(metaclass=Singleton):
    def __init__(self):
        self.__billingService = BillingService()

    def getGrossRevenue(self, month: int):
        return self.__billingService.getGrossRevenue(month)

    def getNetRevenue(self, month: int):
        return self.__billingService.getNetRevenue(month)

    def getEmployeeWages(self, month: int):
        return self.__billingService.getEmployeeWages(month)

    def getTaxes(self, month: int):
        return self.__billingService.getTaxes(month)

    def getMonths(self):
        return {
            "Nenhum mês selecionado": 0,
            "Janeiro": 1,
            "Fevereiro": 2,
            "Março": 3,
            "Abril": 4,
            "Maio": 5,
            "Junho": 6,
            "Julho": 7,
            "Agosto": 8,
            "Setembro": 9,
            "Outubro": 10,
            "Novembro": 11,
            "Dezembro": 12,
        }
