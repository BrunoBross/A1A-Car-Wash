from package.app.meta.Singleton import Singleton
from package.app.api.modules.SchedulingState.SchedulingStateController import SchedulingStateController
from package.app.api.modules.Scheduling.SchedulingController import SchedulingController
from package.app.api.modules.job.JobController import JobController
from package.app.api.modules.vehicle.VehicleController import VehicleController
from package.app.api.modules.employee.EmployeeController import EmployeeController
from package.app.client.state.ComponentState import ComponentState
from package.app.api.modules.SchedulingState.dto.SchedulingStateDto import SchedulingStateDto
from package.app.api.modules.Scheduling.dto.SchedulingDto import SchedulingDto
from package.app.api.modules.job.dto.JobDto import JobDto
from package.app.api.modules.vehicle.dto.VehicleDto import VehicleDto
from package.app.api.modules.employee.dto.EmployeeDto import EmployeeDto



class EmployeeSchedulingComponent(metaclass=Singleton):

    def __init__(self):
        self.__SchedulingStateController = SchedulingStateController()
        self.__SchedulingController = SchedulingController()
        self.__JobController = JobController()
        self.__VehicleController = VehicleController()
        self.__EmployeeController = EmployeeController()
        self.__state = ComponentState()

    #esse cara faz a logica
    #Seleciona o cara na lista
    #Seleciona o estado dele

    def getAllSchedulingStates(self) -> SchedulingStateDto:
        return self.__SchedulingStateController.getAll()

    def getAllScheduling(self) -> SchedulingDto:
        return self.__SchedulingController.getAll()

    def getJobById(self, id:int) -> JobDto:
        return self.__JobController.getJobById(id)

    def getVehicleByPlate(self, plate:int) -> VehicleDto:
        return self.__VehicleController.getVehicleByPlate(plate)

    def getVehicleById(self, id:int) -> VehicleDto:
        return self.__VehicleController.getVehicleById(id)

    def getEmployeeByUserID(self, userID:int) -> EmployeeDto:
        return self.__EmployeeController.getEmployeeByUserId(userID)

    def getSchedulingByEmployeeID(self, employeeID:int):
        return self.__SchedulingController.getByEmployeeId(employeeID)