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
        # PEGANDO O PREÇO DE TODOS OS SERVIÇOS FINALIZADOS NO MES
        grossRevenue = 0
        schedulings = self.__billingQuery.getGrossRevenue(start_date, end_date)
        for scheduling in schedulings:
            grossRevenue += scheduling.job.cost_value
        return grossRevenue

    def getNetRevenue(self, start_date: str, end_date: str):
        # SUBTRAINDO DO FATURAMENTO BRUTO O SALARIO E AS TAXAS
        netRevenue = self.getGrossRevenue(start_date, end_date)\
                     - self.getEmployeeWages(start_date, end_date)\
                     - self.getTaxes(start_date, end_date)
        return netRevenue

    def getEmployeeWages(self, start_date: str, end_date: str):
        # PEGANDO O SALARIO DESCONTANDO O IRPF MENSAL DE 15%
        employeeWages = 0
        employeeList = self.__billingQuery.getEmployeeWages(end_date)
        for employee in employeeList:
            employeeWages += employee.wage - employee.wage * 0.15

        # DA OS 20% DE PENALIDADE AO SALARIO NOS SERVICOS QUE ESTAO PENDENTES E PASSAM DA DATA
        schedulingNotFinalized = self.__billingQuery.getSchedulingNotFinalized(start_date, end_date)
        for scheduling in schedulingNotFinalized:
            print(scheduling.job.cost_value)
            employeeWages -= scheduling.job.cost_value * 0.2

        return employeeWages

    def getTaxes(self, start_date: str, end_date: str):
        # APLICANDO A TAXA DE JUSTA CAUSA E SEM JUSTA CAUSA DOS FUNCIONARIOS DEMITIDOS
        totalTaxes = 0
        taxes = self.__billingQuery.getTaxes(start_date, end_date)
        for tax in taxes:
            employee = self.__employeeQuery.getEmployeeById(tax.employee_id)
            if tax.resignation_type.description == "SEM_JUSTA_CAUSA":
                totalTaxes += employee.wage * 2     # SALARIO + DECIMO TERCEIRO
            elif tax.resignation_type.description == "JUSTA_CAUSA":
                totalTaxes += employee.wage         # APENAS SALARIO

        # ADICIONANDO AOS IMPOSTOS E TAXAS AS COMISSOES DE 20% DOS FUNCIONARIOS
        totalTaxes += self.getGrossRevenue(start_date, end_date) * 0.2

        # ADICIONANDO AOS IMPOSTOS E TAXAS O IRPF MENSAL DE 15% DOS SALARIOS DOS FUNCIONARIOS
        totalTaxes += self.getEmployeeWages(start_date, end_date) * 0.15
        return totalTaxes
