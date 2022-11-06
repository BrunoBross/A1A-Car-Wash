from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO
from package.app.api.model.Employee import Employee
from package.app.api.model.Scheduling import Scheduling
from package.app.api.model.Resignation import Resignation
from package.app.api.model.ResignationType import ResignationType
from package.app.api.model.Job import Job


class BillingQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()

    def getGrossRevenue(self, month: int):
        #TODO: filtrar pelo mes
        return self.__dao.select(Scheduling).join(Job, Scheduling.job_id == Job.id).all()

    def getActiveEmployeeWages(self, month: int):
        #TODO: filtrar pelo mes
        return self.__dao.select(Employee).where(Employee.active_register == 1).all()

    def getTaxes(self, month: int):
        # TODO: filtrar pelo mes
        return self.__dao.select(Resignation).join(ResignationType, Resignation.resignation_type_id == ResignationType.id).all()
