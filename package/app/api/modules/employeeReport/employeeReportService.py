from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO
from package.app.api.modules.billing.BillingQuery import BillingQuery
from package.app.api.modules.employee.EmployeeService import EmployeeService
from package.app.api.modules.Scheduling.SchedulingService import SchedulingService
from package.app.api.modules.job.JobService import JobService
from datetime import datetime

class EmployeeReportService(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()
        self.__billingQuery = BillingQuery()
        self.__employeeService = EmployeeService()
        self.__schedulingService = SchedulingService()
        self.__jobService = JobService()


    def getEmployeeReport(self, employeeID:int, startMonth:str, endMonth:str):
        print(employeeID)
        print(startMonth)
        print(endMonth)
        employee = self.__employeeService.getEmployeeById(employeeID)
        print("EMPLOYEE OBJ")
        print(employee)
        print("EMPLOYEE ID")
        print(employee.id)
        print("EMPLOYEE NAME")
        print(employee.legalName)
        employeeNome = employee.legalName
        
        valorSchedulingsTotal = 0
        totalComissoes = 0
        SalarioBruto = employee.wage
        totalPenalidades = 0

        schedulings = self.__schedulingService.getSchedulingByEmployeeIDAndDate(employeeID, startMonth,endMonth)
        print("SCHEDULIGNS**************************************")
        print(schedulings)
        for item in schedulings:
            print("ITENS BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
            print(item)
            print(item.job_id)
            print(item.job_state_id)
            if item.job_state_id == 2:
                job = self.__jobService.getJobById(item.job_id)
                print("FINALIZADO AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                print("CONSULTA")
                print(job)
                print(job.description)
                print(job.cost_value)
                valorSchedulingsTotal += job.cost_value
                comissao = job.cost_value * 0.2
                print("COMISSAO")
                print(comissao)
                totalComissoes += comissao
            elif item.job_state_id == 1 and item.date < datetime.today().date():
                print("PENDENTE")
                print("CONSULTA")
                job = self.__jobService.getJobById(item.job_id)
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

        return [employeeNome, valorSchedulingsTotal, SalarioBruto, SalarioLiquido, totalComissoes, totalPenalidades]
