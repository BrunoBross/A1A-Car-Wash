from package.app.meta.Singleton import Singleton
from package.app.api.modules.billing.BillingController import BillingController


class BillingComponent(metaclass=Singleton):
    def __init__(self):
        self.__billingController = BillingController()

    def getBilling(self, month: str):
        start_date = self.__billingController.getStartMonthFormat(month)
        end_date = self.__billingController.getEndMonthFormat(month)

        return self.__billingController.getBilling(start_date, end_date)
