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
        # pegando os valores dos serviços
        grossRevenue = 0
        schedulings = self.__billingQuery.getGrossRevenue(month)
        for scheduling in schedulings:
            grossRevenue += scheduling.job.cost_value
        return grossRevenue

    def getNetRevenue(self, month: int):
        # pegando o faturamento bruto e deduzindo salarios e impostos
        netRevenue = self.getGrossRevenue(month) - self.getEmployeeWages(month) - self.getTaxes(month)
        return netRevenue

    def getEmployeeWages(self, month: int):
        # está adicionando o salario dos funcionários ativos (desconta o irpf para mostrar nos impostos)
        employeeWages = 0
        employees = self.__billingQuery.getActiveEmployeeWages(month)
        for employee in employees:
            employeeWages += employee.wage - employee.wage * 0.15
        return employeeWages

    def getTaxes(self, month: int):
        # está adicionando a taxa do decimo terceiro do funcionario demitido sem justa causa,
        # comissoes pelos serviços e irpf
        totalTaxes = 0
        taxes = self.__billingQuery.getTaxes(month)
        for tax in taxes:
            employee = self.__employeeQuery.getEmployeeById(tax.employee_id)
            if tax.resignation_type.description == "SEM_JUSTA_CAUSA":
                totalTaxes += employee.wage
        totalTaxes += self.getGrossRevenue(month) * 0.2
        totalTaxes += self.getEmployeeWages(month) * 0.15
        return totalTaxes
