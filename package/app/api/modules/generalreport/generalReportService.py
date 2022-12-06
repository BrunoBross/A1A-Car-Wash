from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO
from package.app.api.modules.billing.BillingQuery import BillingQuery
from package.app.api.modules.employee.EmployeeService import EmployeeService
from package.app.api.modules.Scheduling.SchedulingService import SchedulingService
from package.app.api.modules.job.JobService import JobService
from datetime import datetime

class GeneralReportService(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()
        self.__billingQuery = BillingQuery()
        self.__employeeService = EmployeeService()
        self.__schedulingService = SchedulingService()
        self.__jobService = JobService()