from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO
from package.app.api.modules.billing.BillingQuery import BillingQuery
from package.app.api.modules.employee.EmployeeQuery import EmployeeQuery


class BillingService(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()
        self.__billingQuery = BillingQuery()
        self.__employeeQuery = EmployeeQuery()

    def getGrossRevenue(self, month: int):
        # TA PEGANDO OS VALORES DOS SERVICOS
        grossRevenue = 0
        schedulings = self.__billingQuery.getGrossRevenue(month)
        for scheduling in schedulings:
            grossRevenue += scheduling.job.cost_value
        return grossRevenue

    def getNetRevenue(self, month: int):
        netRevenue = self.getGrossRevenue(month) - self.getEmployeeWages() - self.getTaxes(month)
        return netRevenue

    def getEmployeeWages(self):
        # TA PEGANDO O SALARIO DE TODOS OS FUNCIONARIOS ATIVOS
        employeeWages = 0
        employees = self.__billingQuery.getEmployeeWages()
        for employee in employees:
            employeeWages += employee.wage
        return employeeWages

    def getTaxes(self, month: int):
        # TA PEGANDO AS DEMISSOES APENAS
        totalTaxes = 0
        taxes = self.__billingQuery.getTaxes(month)
        for tax in taxes:
            employee = self.__employeeQuery.getEmployeeById(tax.employee_id)
            if tax.resignation_type.description == "SEM_JUSTA_CAUSA":
                totalTaxes += float(employee.wage) * 0.2
        return totalTaxes
