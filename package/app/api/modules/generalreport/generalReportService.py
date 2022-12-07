from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO
from package.app.api.modules.billing.BillingQuery import BillingQuery
from package.app.api.modules.employee.EmployeeService import EmployeeService
from package.app.api.modules.Scheduling.SchedulingService import SchedulingService
from package.app.api.modules.resignation.ResignationService import ResignationService
from package.app.api.modules.job.JobService import JobService
from datetime import datetime

class GeneralReportService(metaclass=Singleton):
    def __init__(self):
        self.__resignationService = ResignationService()
        self.__employeeService = EmployeeService()
        self.__schedulingService = SchedulingService()

    def getGeneralReport(self, startMonth:str, endMonth:str):
           
        servicedVehicles = 0
        numberOfServices = 0
        numberOfEmployees = 0
        customerAbscences = 0

        finishedServicesByMonth = self.__schedulingService.getAllFinishedByMonth(startMonth, endMonth)

        # NUMBER OF SERVICED VEHICLES
        finishedServicesVehicleId = []
        for i in finishedServicesByMonth:
            finishedServicesVehicleId.append(i.vehicle_id)
        servicedVehicles = len(self.distinct(finishedServicesVehicleId))
        
        # NUMBER OF FINISHED SERVICES
        numberOfServices = len(finishedServicesByMonth)
        
        # NUMBER OF EMPLOYEES
        admitted_until_end_date_employees = self.__employeeService \
            .getEmployeesByAdmissionDate(endMonth)
        resignated_after_start_date_employees_id = self.fromTupleToInt(
            self.__resignationService.getResignatedEmployeeAfterDateId(startMonth))
        
        numberOfEmployees = len(self.getValidEmployees(
            admitted_until_end_date_employees,
            resignated_after_start_date_employees_id
        ))

        # NUMBER OF CUSTOMER ABSCENCES
        customerAbscences = len(
            self.__schedulingService.getAllClientAbscencesByMonth(endMonth, startMonth))

        reportData = []

        if len(str(servicedVehicles)) == 1:
            reportData.append(f'0{servicedVehicles}')
        else:
            reportData.append(servicedVehicles)

        if len(str(numberOfServices)) == 1:
            reportData.append(f'0{numberOfServices}')
        else:
            reportData.append(servicedVehicles)
        
        if len(str(numberOfEmployees)) == 1:
            reportData.append(f'0{numberOfEmployees}')
        else:
            reportData.append(servicedVehicles)

        if len(str(customerAbscences)) == 1:
            reportData.append(f'0{servicedVehicles}')
        else:
            reportData.append(customerAbscences)

        return reportData
    
    
    def distinct(self, list) -> list:
        distinct_list = []
        for i in list:
            if i not in distinct_list:
                distinct_list.append(i)
        return distinct_list

    def getValidEmployees(
        self,
        admitted_until_end_date_employees,
        resignated_after_start_date_employees_id
    ):
        employees = []
        for employee in admitted_until_end_date_employees:
            if employee.id not in resignated_after_start_date_employees_id:
                employees.append(employee)
        return employees

    def fromTupleToInt(self,resignated_employees_id):
        result = []
        for i in resignated_employees_id:
            result.append(i[0])
        return result