from dataclasses import dataclass, field
from datetime import date, datetime
from typing import List
from package.app.api.modules.employee.EmployeeController import EmployeeController
from package.app.api.modules.employee.dto.EmployeeDto import EmployeeDto
from package.app.api.modules.job.JobController import JobController
from package.app.api.modules.job.dto.JobDto import JobDto
from package.app.api.modules.scheduling.SchedulingController import SchedulingController
from package.app.api.modules.scheduling.dto.SchedulingDto import SchedulingDto
from package.app.api.modules.vehicle.VehicleController import VehicleController
from package.app.api.modules.vehicle.dto.VehicleDto import VehicleDto
from package.app.client.dialog.DialogService import DialogService
from package.app.client.dialog.InfoBox import InfoBoxProps
from package.app.client.event.EventManager import EventManager
from package.app.client.gui.box.Box import Box
from package.app.client.modules.registerscheduling.RegisterSchedulingValidator import (
    SchedulingValidator,
)
from package.app.client.state.ComponentState import ComponentState
from package.app.client.utils.form import safeCastIdToInt
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk
from package.app.validation.IValidator import IValidator


@dataclass
class RegisterSchedulingComponentInfo:
    employees: List[EmployeeDto] = field(default_factory=list)
    jobs: List[JobDto] = field(default_factory=list)
    vehicles: List[VehicleDto] = field(default_factory=list)


class RegisterSchedulingComponent(metaclass=Singleton):
    def __init__(self):
        self.__state = ComponentState()
        self.__validator: IValidator = SchedulingValidator()
        self.__schedulingController = SchedulingController()
        self.__employeeController = EmployeeController()
        self.__vehicleController = VehicleController()
        self.__jobController = JobController()
        self.__dialogService = DialogService()
        self.__eventManager = EventManager()

    def requestRegisterScheduling(self):
        dto = SchedulingDto(
            employee=EmployeeDto(
                id=safeCastIdToInt(
                    self.__state.getReferenceById("funcionario").get_active_id()
                )
            ),
            vehicle=VehicleDto(
                id=safeCastIdToInt(
                    self.__state.getReferenceById("veiculo").get_active_id()
                )
            ),
            job=JobDto(
                id=safeCastIdToInt(
                    self.__state.getReferenceById("servico").get_active_id()
                )
            ),
            date=self.__parseCalendarResultTuple(
                self.__state.getReferenceById("data").get_date(),
            ),
        )

        if self.__validator.execute(dto):
            entity = self.__schedulingController.registerScheduling(dto)
            if entity:
                self.__displaySuccessMessage()

    def getState(self) -> ComponentState:
        return self.__state

    def fetchInfo(self) -> RegisterSchedulingComponentInfo:
        return RegisterSchedulingComponentInfo(
            employees=self.__employeeController.getEmployees(),
            jobs=self.__jobController.getJobs(),
            vehicles=self.__vehicleController.getVehicles(),
        )

    @property
    def eventManager(self) -> EventManager:
        return self.__eventManager

    def __parseCalendarResultTuple(self, tuple) -> datetime.date:
        return date(year=tuple.year, month=tuple.month + 1, day=tuple.day)

    def __displaySuccessMessage(self):
        content = Box()
        content.pack_default(Gtk.Label("Agendamento cadastrado com sucesso"))
        self.__dialogService.displayInfoBox(
            InfoBoxProps(title="Cadastro bem sucedido", content=content)
        )
