from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO
from package.app.api.modules.billing.BillingQuery import BillingQuery
from package.app.api.modules.employee.EmployeeQuery import EmployeeQuery


class BillingService(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()
        self.__billingQuery = BillingQuery()
        self.__employeeQuery = EmployeeQuery()

    def getGrossRevenue(self, start_date: str, end_date: str):
        # TA PEGANDO OS VALORES DOS SERVICOS
        grossRevenue = 0
        schedulings = self.__billingQuery.getGrossRevenue(start_date, end_date)
        for scheduling in schedulings:
            grossRevenue += scheduling.job.cost_value
        return grossRevenue

    def getNetRevenue(self, start_date: str, end_date: str):
        netRevenue = self.getGrossRevenue(start_date, end_date) - self.getEmployeeWages(end_date) - self.getTaxes(start_date, end_date)
        return netRevenue

    def getEmployeeWages(self, end_date: str):
        # TA PEGANDO O SALARIO DE TODOS OS FUNCIONARIOS ATIVOS
        employeeWages = 0
        employeeList = self.__billingQuery.getEmployeeWages(end_date)
        for employee in employeeList:
            employeeWages += employee.wage
        return employeeWages

    def getTaxes(self, start_date: str, end_date: str):
        # TA PEGANDO AS DEMISSOES APENAS
        totalTaxes = 0
        taxes = self.__billingQuery.getTaxes(start_date, end_date)
        for tax in taxes:
            employee = self.__employeeQuery.getEmployeeById(tax.employee_id)
            if tax.resignation_type.description == "SEM_JUSTA_CAUSA":
                totalTaxes += float(employee.wage) * 0.2
        return totalTaxes
