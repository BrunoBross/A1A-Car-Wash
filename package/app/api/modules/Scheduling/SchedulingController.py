from package.app.meta.Singleton import Singleton
from package.app.api.modules.Scheduling.SchedulingService import SchedulingService
from package.app.api.modules.vehicle.VehicleService import VehicleService
from package.app.api.modules.SchedulingState.SchedulingStateService import SchedulingStateService
from package.app.api.modules.job.JobService import JobService
from package.app.api.modules.Scheduling.dto.SchedulingDto import SchedulingDto

class SchedulingController(metaclass=Singleton):
    def __init__(self):
        self.__SchedulingService = SchedulingService()
        self.__VehicleService = VehicleService()
        self.__JobService = JobService()
        self.__SchedulingStateService = SchedulingStateService()

    def getAll(self) -> SchedulingDto:
        return self.__SchedulingService.getAll()

    def getByEmployeeId(self, employeeId:int) -> SchedulingDto:
        return self.__SchedulingService.getByEmployeeId(employeeId)

    def getJobIdByName(self, description: str):
        job = self.__JobService.getJobByDescription(description)
        return job.id

    def getVehicleIdByPlate(self, plate: str):
        vehicle = self.__VehicleService.getVehicleByPlate(plate)
        return vehicle.id

    def getJobStateIdByName(self, description: str):
        schedulingState = self.__SchedulingStateService.getSchedulingStateByDescription(description)
        return schedulingState.id

    def updateJobStateID(self, employeeId: int, scheduling: list, job_state: str):
        vehicle = scheduling[0]
        job = scheduling[1]
        date = scheduling[2]
        self.__SchedulingService.updateJobStateID(employeeId,
                                                  self.getJobIdByName(job),
                                                  self.getVehicleIdByPlate(vehicle),
                                                  date,
                                                  self.getJobStateIdByName(job_state))
