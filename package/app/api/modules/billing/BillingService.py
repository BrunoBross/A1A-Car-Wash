from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO
from package.app.api.model.Scheduling import Scheduling


class BillingService(metaclass=Singleton):
    def __int__(self):
        self.__dao = DAO()

    def getGrossRevenue(self, month: str):
        return self.__dao.select(Scheduling.job.cost_value).where(Scheduling.job_state == "FINALIZADO")

    def getNetRevenue(self, month: str):
        return 9000

    def getEmployeeWages(self, month: str):
        return 5000

    def getTaxes(self, month: str):
        return 1000
