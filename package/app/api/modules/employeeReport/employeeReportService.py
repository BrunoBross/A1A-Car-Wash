from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO
from package.app.api.modules.billing.BillingQuery import BillingQuery
from package.app.api.modules.employee.EmployeeQuery import EmployeeQuery
from package.app.api.modules.scheduling.SchedulingQuery import SchedulingQuery
from package.app.api.modules.job.JobQuery import JobQuery
from datetime import datetime

class EmployeeReportService(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()
        self.__billingQuery = BillingQuery()
        self.__employeeQuery = EmployeeQuery()
        self.__schedulingQuery = SchedulingQuery()
        self.__jobQuery = JobQuery()


    def getEmployeeReport(self, employeeID:int, startMonth:str, endMonth:str):
        employee = self.__employeeQuery.getEmployeeById(employeeID)
        
        valorSchedulingsTotal = 0
        totalComissoes = 0
        SalarioBruto = employee.wage
        totalPenalidades = 0

        schedulings = self.__schedulingQuery.getSchedulingByEmployeeIDAndDate(employeeID, startMonth, endMonth)
        print("SCHEDULIGNS")
        print(schedulings)
        for item in schedulings:
            print("ITENS")
            print(item)
            if item.job_state_id == 2:
                job = self.__jobQuery.getJobNyId(item.job_id)
                print("FINALIZADO")
                print("CONSULTA")
                print(job)
                print(job.description)
                print(job.cost_value)
                valorSchedulingsTotal += job.cost_value
                comissao = job.cost_value * 0.2
                print("COMISSAO")
                print(comissao)
                totalComissoes += comissao
            elif item.job_state_id == 1 and item.date < datetime.today():
                print("PENDENTE")
                print("CONSULTA")
                job = self.__jobQuery.getJobNyId(item.job_id)
                print(job)
                print(job.description)
                print(job.cost_value)
                penalidade = job.cost_value * 0.2
                print("PENALIDADE")
                print(penalidade)
                totalPenalidades += penalidade
        
        SalarioBruto += totalComissoes
        SalarioLiquido = SalarioBruto - totalPenalidades

        print("TOTAL SCHEDULINGS")
        print(valorSchedulingsTotal)
        print("SALARIO BRUTO")
        print(SalarioBruto)
        print("SALARIO LIQUIDO")
        print(SalarioLiquido)
        print("TOTAL COMISSOES")
        print(totalComissoes)
        print("TOTAL PENALIDADES")
        print(totalPenalidades)

        return [valorSchedulingsTotal, SalarioBruto, SalarioLiquido, totalComissoes, totalPenalidades]
