from package.app.meta.Singleton import Singleton
from package.app.api.modules.SchedulingState.SchedulingStateController import (
    SchedulingStateController,
)
from package.app.api.modules.Scheduling.SchedulingController import SchedulingController
from package.app.api.modules.job.JobController import JobController
from package.app.api.modules.vehicle.VehicleController import VehicleController
from package.app.api.modules.employee.EmployeeController import EmployeeController
from package.app.client.state.ComponentState import ComponentState
from package.app.api.modules.SchedulingState.dto.SchedulingStateDto import (
    SchedulingStateDto,
)
from package.app.api.modules.Scheduling.dto.SchedulingDto import SchedulingDto
from package.app.api.modules.job.dto.JobDto import JobDto
from package.app.api.modules.vehicle.dto.VehicleDto import VehicleDto
from package.app.api.modules.employee.dto.EmployeeDto import EmployeeDto
from package.app.client.state.UserContext import UserContext
from package.app.client.dialog.DialogService import DialogService
from package.app.api.modules.warning.WarningService import WarningService
from package.app.client.gui.box.Box import Box
from package.app.client.gui.imports import Gtk
from package.app.client.dialog.InfoBox import InfoBoxProps


class EmployeeSchedulingComponent(metaclass=Singleton):
    def __init__(self):
        self.__SchedulingStateController = SchedulingStateController()
        self.__SchedulingController = SchedulingController()
        self.__JobController = JobController()
        self.__VehicleController = VehicleController()
        self.__EmployeeController = EmployeeController()
        self.__state = ComponentState()
        self.__userContext = UserContext()
        self.__dialogService = DialogService()
        self.__warningService = WarningService()

    def getWarningList(self):
        warningList = []
        warning_table = self.__warningService.getWarningList(self.getLoggedEmployee().id)
        for item in warning_table:
            warningList.append([item.id, item.warning.description, item.read])
        if len(warningList) > 0:
            return warningList
        return [["Nenhum aviso disponível", False]]

    def changeWarningReadStatus(self, warning_id: int, read_bool: bool):
        self.__warningService.changeWarningReadStatus(warning_id, read_bool)

    def getLoggedEmployee(self):
        user_id = self.__userContext.get().id
        return self.getEmployeeByUserID(user_id)

    def getAllSchedulingStates(self) -> SchedulingStateDto:
        return self.__SchedulingStateController.getAll()

    def getAllScheduling(self) -> SchedulingDto:
        return self.__SchedulingController.getAll()

    def getJobById(self, id: int) -> JobDto:
        return self.__JobController.getJobById(id)

    def getVehicleByPlate(self, plate: int) -> VehicleDto:
        return self.__VehicleController.getVehicleByPlate(plate)

    def getVehicleById(self, id: int) -> VehicleDto:
        return self.__VehicleController.getVehicleById(id)

    def getEmployeeByUserID(self, userID: int) -> EmployeeDto:
        return self.__EmployeeController.getEmployeeByUserId(userID)

    def getSchedulingByEmployeeID(self, employeeID: int):
        return self.__SchedulingController.getByEmployeeId(employeeID)

    def updateJobStateID(self, scheduling: list, job_state: str):
        if self.__SchedulingController.updateJobStateID(
            self.getLoggedEmployee().id, scheduling, job_state
        ):
            self.__displaySuccessMessage()

    def getSchedulingList(self):
        schedulings = self.getSchedulingByEmployeeID(self.getLoggedEmployee().id)
        itemsList = []
        for i in schedulings:
            job = self.getJobById(i.job_id)
            vehicle = self.getVehicleById(i.vehicle_id)
            itemsList.append((vehicle.numberPlate, job.description, str(i.date)))
        if itemsList:
            return itemsList
        else:
            return [["Nenhum agendamento pendente", None, None]]

    def getState(self) -> ComponentState:
        return self.__state

    def __displaySuccessMessage(self):
        content = Box()
        content.pack_default(Gtk.Label("Serviço finalizado com sucesso"))
        self.__dialogService.displayInfoBox(
            InfoBoxProps(title="Finalização bem sucedida", content=content)
        )
