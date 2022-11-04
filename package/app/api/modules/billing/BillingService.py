from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO
from package.app.api.model.Scheduling import Scheduling
from package.app.api.model.Job import Job
from package.app.api.model.Employee import Employee


class BillingService(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()

    def getGrossRevenue(self, month: int):
        schedulings = self.__dao.select(Scheduling).join(Job, Scheduling.job_id == Job.id).all()
        for scheduling in schedulings:
            print(scheduling)
        return 15000

    def getNetRevenue(self, month: int):
        netRevenue = self.getGrossRevenue(month) - self.getEmployeeWages() - self.getTaxes(month)
        return netRevenue

    def getEmployeeWages(self):
        employeeWages = 0
        employees = self.__dao.select(Employee).all()
        for employee in employees:
            employeeWages += employee.wage
        return employeeWages

    def getTaxes(self, month: int):
        return 1000
