from package.app.meta.Singleton import Singleton
from package.app.api.modules.billing.BillingController import BillingController
from package.app.client.state.ComponentState import ComponentState


class BillingComponent(metaclass=Singleton):
    def __init__(self):
        self.__billingController = BillingController()
        self.__state = ComponentState()

    def getBilling(self, month: str):
        start_date = self.__billingController.getStartMonthFormat(month)
        end_date = self.__billingController.getEndMonthFormat(month)

        return [self.__billingController.getGrossRevenue(start_date, end_date),
                self.__billingController.getNetRevenue(start_date, end_date),
                self.__billingController.getEmployeeWages(start_date, end_date),
                self.__billingController.getTaxes(start_date, end_date)]

    def getState(self) -> ComponentState:
        return self.__state
