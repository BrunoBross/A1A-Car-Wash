from package.app.meta.Singleton import Singleton
from package.app.api.modules.billing.BillingController import BillingController
from package.app.client.state.ComponentState import ComponentState


class BillingComponent(metaclass=Singleton):
    def __init__(self):
        self.__billingController = BillingController()
        self.__state = ComponentState()

    def getGrossRevenue(self):
        return self.__billingController.getGrossRevenue("1")

    def getNetRevenue(self):
        return self.__billingController.getNetRevenue("1")

    def getEmployeeWages(self):
        return self.__billingController.getEmployeeWages("1")

    def getTaxes(self):
        return self.__billingController.getTaxes("1")

    def getState(self) -> ComponentState:
        return self.__state
