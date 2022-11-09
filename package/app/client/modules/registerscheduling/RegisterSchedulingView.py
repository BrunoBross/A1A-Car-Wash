from package.app.client.event.EventEnum import EventEnum
from package.app.client.gui.box.Box import Box
from package.app.client.modules.registerscheduling.RegisterSchedulingComponent import (
    RegisterSchedulingComponent,
)
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk


class RegisterSchedulingView(metaclass=Singleton):
    def __init__(self):
        self.__component = RegisterSchedulingComponent()
        self.__employeeSelectInput: Gtk.ComboBoxText
        self.__jobSelectInput: Gtk.ComboBoxText
        self.__vehicleSelectInput: Gtk.ComboBoxText
        self.__dateCalendarInput: Gtk.Calendar
        self.__subscribeSetup()

    def get(self) -> Gtk.Box:
        mainBox = Box()
        topRow = Box()
        bottomRow = Box()
        leftColumn = Box()
        rightColumn = Box()

        mainBox.set_orientation(Gtk.Orientation.VERTICAL)
        topRow.set_orientation(Gtk.Orientation.HORIZONTAL)
        leftColumn.set_orientation(Gtk.Orientation.VERTICAL)
        rightColumn.set_orientation(Gtk.Orientation.VERTICAL)

        self.__employeeSelectInput = Gtk.ComboBoxText()
        self.__jobSelectInput = Gtk.ComboBoxText()
        self.__vehicleSelectInput = Gtk.ComboBoxText()
        self.__dateCalendarInput = Gtk.Calendar()
        confirmButton = Gtk.Button("Confirmar")

        self.__jobSelectInput.set_margin_bottom(5)
        self.__employeeSelectInput.set_margin_bottom(5)

        leftColumn.pack_start(self.__employeeSelectInput, False, False, 0)
        leftColumn.pack_start(self.__vehicleSelectInput, False, False, 0)
        rightColumn.pack_start(self.__jobSelectInput, False, False, 0)
        rightColumn.pack_start(confirmButton, False, False, 0)

        rightColumn.set_margin_top(5)
        rightColumn.set_margin_right(5)
        rightColumn.set_margin_bottom(5)
        rightColumn.set_margin_left(5)

        leftColumn.set_margin_top(5)
        leftColumn.set_margin_right(5)
        leftColumn.set_margin_bottom(5)
        leftColumn.set_margin_left(5)

        topRow.pack_default(leftColumn)
        topRow.pack_default(rightColumn)
        bottomRow.pack_default(self.__dateCalendarInput)
        mainBox.pack_default(topRow)
        mainBox.pack_default(bottomRow)

        confirmButton.connect("clicked", self.__onConfirm)

        return mainBox

    def __setInputData(self) -> None:
        data = self.__component.fetchInfo()

        for employee in data.employees:
            print(employee)
            self.__employeeSelectInput.append(
                id=f"{employee.id}",
                text=f"[{employee.user.username}] {employee.legalName}",
            )

        for job in data.jobs:
            self.__jobSelectInput.append(
                id=f"{job.id}", text=f"{job.description} - ${job.cost_value}"
            )

        for vehicle in data.vehicles:
            self.__vehicleSelectInput.append(
                id=f"{vehicle.id}", text=vehicle.numberPlate
            )

    def __clearInputData(self):
        self.__employeeSelectInput.remove_all()
        self.__jobSelectInput.remove_all()
        self.__vehicleSelectInput.remove_all()

    def __reset(self, _):
        self.__clearInputData()
        self.__setInputData()

    def __onConfirm(self, _: Gtk.Widget):
        self.__component.getState().addReference(
            "funcionario", self.__employeeSelectInput
        )
        self.__component.getState().addReference("veiculo", self.__vehicleSelectInput)
        self.__component.getState().addReference("servico", self.__jobSelectInput)
        self.__component.getState().addReference("data", self.__dateCalendarInput)
        self.__component.requestRegisterScheduling()

    def __subscribeSetup(self):
        self.__component.eventManager.subscribe(EventEnum.SWITCH_VIEW, self.__reset)
        self.__component.eventManager.subscribe(EventEnum.SUBMIT_SUCCESS, self.__reset)
