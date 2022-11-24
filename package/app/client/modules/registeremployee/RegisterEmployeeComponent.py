from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.api.modules.employee.dto.EmployeeDto import EmployeeDto
from package.app.client.dialog.DialogService import DialogService
from package.app.client.dialog.InfoBox import InfoBoxProps
from package.app.client.dialog.Modal import ModalProps
from package.app.client.gui.box.Box import Box
from package.app.client.modules.registeremployee.RegisterEmployeeValidator import (
    RegisterEmployeeValidator,
)
from package.app.meta.Singleton import Singleton
from package.app.api.modules.employee.EmployeeController import EmployeeController
from package.app.client.state.ComponentState import ComponentState
from package.app.client.utils.form import getEntryBuffer
from package.app.client.gui.imports import Gtk
from package.app.validation.IValidator import IValidator
from package.app.exception.DatabaseIntegrityException import DatabaseIntegrityException


class RegisterEmployeeComponent(metaclass=Singleton):
    def __init__(self):
        self.__employeeController = EmployeeController()
        self.__state = ComponentState()
        self.__validator: IValidator = RegisterEmployeeValidator()
        self.__dialogService = DialogService()

    def requestRegisterEmployee(self):
        employeeDto = EmployeeDto(
            legalName=getEntryBuffer(self.__state.getReferenceById("fullname")),
            wage=getEntryBuffer(self.__state.getReferenceById("salary")),
            jobLimit=getEntryBuffer(self.__state.getReferenceById("limit")),
        )
        authDto = AuthDto(
            username=getEntryBuffer(self.__state.getReferenceById("username")),
            password=getEntryBuffer(self.__state.getReferenceById("password")),
        )

        if self.__validator.execute(employeeDto, authDto, False):
            entity = self.__employeeController.registerEmployee(
                employeeDto=employeeDto, authDto=authDto
            )
            if entity:
                self.__displaySuccessMessage("Funcionário cadastrado com sucesso", "Cadastro bem sucedido")

    def requestEditEmployee(self, employee: list):
        if employee is None:
            self.__displaySuccessMessage("Nenhum funcionário selecionado", "Erro")
            return

        user_id = employee[0]

        employeeDto = EmployeeDto(
            legalName=getEntryBuffer(self.__state.getReferenceById("fullnameEdit")),
            wage=getEntryBuffer(self.__state.getReferenceById("salaryEdit")),
            jobLimit=getEntryBuffer(self.__state.getReferenceById("limitEdit")),
        )
        authDto = AuthDto(
            username=getEntryBuffer(self.__state.getReferenceById("usernameEdit")),
            password=getEntryBuffer(self.__state.getReferenceById("passwordEdit")),
        )

        if self.__validator.execute(employeeDto, authDto, True):
            if self.__displayConfirmBox(employee, "editar"):
                try:
                    self.__employeeController.editEmployee(employeeDto=employeeDto, authDto=authDto, user_id=user_id)
                    return self.__displaySuccessMessage("Funcionário editado com sucesso", "Edição bem sucedida")
                except DatabaseIntegrityException as e:
                    print(e)
                    return self.__displaySuccessMessage("Erro na edição, tente novamente", "Erro")
            else:
                return

    def requestDeleteEmployee(self, employee: list):
        user_id = employee[0]
        if self.__displayConfirmBox(employee, "deletar"):
            try:
                if self.__employeeController.deleteEmployee(user_id):
                    return self.__displaySuccessMessage("Funcionário deletado com sucesso", "Deleção bem sucedida")
                return self.__displaySuccessMessage("O funcionário possui agendamentos cadastrados", "Erro")
            except DatabaseIntegrityException as e:
                print(e)
                return self.__displaySuccessMessage("Erro na deleçao, tente novamente", "Erro")
        else:
            return

    def getEmployeeData(self, user_id: int):
        return self.__employeeController.getEmployeeByUserId(user_id)

    def getEmployeeList(self):
        employees = self.__employeeController.getEmployees()
        employeeList = []
        for employee in employees:
            if employee.activeRegister:
                admission = str(employee.admission_date)
            else:
                admission = "Demitido"
            employeeList.append([employee.user.id, employee.user.username, employee.legalName,
                                 str(employee.wage), employee.jobLimit, admission])
        return employeeList

    def getEmployees(self):
        return self.__employeeController.getEmployees()

    def getState(self) -> ComponentState:
        return self.__state

    def __displaySuccessMessage(self, message: str, title_message: str):
        content = Box()
        content.pack_default(Gtk.Label(message))
        self.__dialogService.displayInfoBox(
            InfoBoxProps(title=title_message, content=content)
        )

    def __displayConfirmBox(self, employee: list, label: str):
        content = Box()
        content.pack_default(Gtk.Label(f"Tem certeza que você deseja {label} o funcionário {employee[2]}?"))
        return self.__dialogService.displayModal(
            ModalProps(title="Confirmação", content=content, cancelLabel="Cancelar", okLabel="Confirmar")
        )
