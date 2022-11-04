from package.app.meta.Singleton import Singleton
from package.app.api.modules.billing.BillingController import BillingController
from package.app.client.state.ComponentState import ComponentState


class BillingComponent(metaclass=Singleton):
    def __init__(self):
        self.__billingController = BillingController()
        self.__state = ComponentState()

    def getBilling(self, month: int):
        return [self.__billingController.getGrossRevenue(month),
                self.__billingController.getNetRevenue(month),
                self.__billingController.getEmployeeWages(),
                self.__billingController.getTaxes(month)]

    def getState(self) -> ComponentState:
        return self.__state
