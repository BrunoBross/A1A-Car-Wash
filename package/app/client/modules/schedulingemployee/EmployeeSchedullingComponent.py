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
from package.app.client.state.UserContext import UserContext
from package.app.client.utils.form import getEntryBuffer


class EmployeeSchedulingComponent(metaclass=Singleton):

    def __init__(self):
        self.__SchedulingStateController = SchedulingStateController()
        self.__SchedulingController = SchedulingController()
        self.__JobController = JobController()
        self.__VehicleController = VehicleController()
        self.__EmployeeController = EmployeeController()
        self.__state = ComponentState()
        self.__userContext = UserContext()

    #esse cara faz a logica
    #Seleciona o cara na lista
    #Seleciona o estado dele

    def getLoggedEmployee(self):
        user_id = self.__userContext.get().id
        return self.getEmployeeByUserID(user_id)

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
    
    def updateJobStateID(self, scheduling: list, job_state: str):
        self.__SchedulingController.updateJobStateID(self.getLoggedEmployee().id, scheduling, job_state)

    def getSchedulingList(self):
        schedulings = self.getSchedulingByEmployeeID(self.getLoggedEmployee().id)
        itemsList = []
        for i in schedulings:
            job = self.getJobById(i.job_id)
            vehicle = self.getVehicleById(i.vehicle_id)
            itemsList.append((vehicle.numberPlate, job.description, str(i.date)))
        return itemsList



    def getState(self) -> ComponentState:
        return self.__state
