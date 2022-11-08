from datetime import datetime
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

    def getGrossRevenue(self, start_date: str, end_date: str):
        # PEGANDO O PREÇO DE TODOS OS SERVIÇOS FINALIZADOS NO MES
        return self.__dao.select(Scheduling) \
            .join(Job, Scheduling.job_id == Job.id) \
            .where(Scheduling.date >= start_date) \
            .where(Scheduling.date <= end_date) \
            .where(Scheduling.job_state_id == 2) \
            .all()

    def getEmployeeWages(self, end_date: str):
        # GAMBIARRA LOCCA PRA PEGAR O EMPLOYEE POR DATA, FILTRANDO SE FOI DEMITIDO NO MES OU NAO
        employees = self.__dao.select(Employee).where(Employee.admission_date <= end_date).all()
        resignations = self.__dao.select(Resignation.employee_id).where(Resignation.date <= end_date).all()
        resignationsIds = []
        for resignation in resignations:
            resignationsIds.append(list(resignation)[0])

        employeeList = []
        for employee in employees:
            if not (employee.id in resignationsIds):
                print(employee.id)
                employeeList.append(employee)

        return employeeList

    def getTaxes(self, start_date: str, end_date: str):
        return self.__dao.select(Resignation) \
            .join(ResignationType, Resignation.resignation_type_id == ResignationType.id) \
            .where(Resignation.date >= start_date) \
            .where(Resignation.date <= end_date) \
            .all()

    def getSchedulingNotFinalized(self, start_date: str, end_date: str):
        return self.__dao.select(Scheduling)\
            .join(Job, Scheduling.job_id == Job.id) \
            .where(Scheduling.date >= start_date) \
            .where(Scheduling.date <= end_date) \
            .where(Scheduling.job_state_id == 1)\
            .where(Scheduling.date >= datetime.now().date())\
            .all()
