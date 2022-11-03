from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.api.modules.employee.dto.EmployeeDto import EmployeeDto
from package.app.client.dialog.DialogService import DialogService
from package.app.client.dialog.InfoBox import InfoBoxProps
from package.app.client.gui.box.Box import Box
from package.app.client.modules.registeremployee.RegisterEmployeeValidator import (
    RegisterEmployeeValidator,
)
from package.app.meta.Singleton import Singleton
from package.app.api.modules.employee.EmployeeController import EmployeeController
from package.app.client.state.ComponentState import ComponentState
from package.app.client.utils.form import getEntryBuffer
from package.app.client.gui.imports import Gtk


class RegisterEmployeeComponent(metaclass=Singleton):
    def __init__(self):
        self.__employeeController = EmployeeController()
        self.__state = ComponentState()
        self.__validator = RegisterEmployeeValidator()
        self.__dialogService = DialogService()

    def requestRegisterEmployee(self):
        employeeDto = EmployeeDto(
            legalName=getEntryBuffer(self.__state.getReferenceById("fullname")),
            wage=getEntryBuffer(self.__state.getReferenceById("salary")),
        )
        authDto = AuthDto(
            username=getEntryBuffer(self.__state.getReferenceById("username")),
            password=getEntryBuffer(self.__state.getReferenceById("password")),
        )

        if self.__validator.execute(employeeDto, authDto):
            entity = self.__employeeController.registerEmployee(
                employeeDto=employeeDto, authDto=authDto
            )
            if entity:
                self.__displaySuccessMessage()

    def getState(self) -> ComponentState:
        return self.__state

    def __displaySuccessMessage(self):
        content = Box()
        content.pack_default(Gtk.Label("Funcionário cadastrado com sucesso"))
        self.__dialogService.displayInfoBox(
            InfoBoxProps(title="Cadastro bem sucedido", content=content)
        )
