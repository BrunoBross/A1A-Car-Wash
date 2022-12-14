from traceback import print_tb
from package.app.api.modules.resignation.ResignationController import ResignationController
from package.app.client.dialog.DialogService import DialogService
from package.app.client.dialog.InfoBox import InfoBoxProps
from package.app.client.gui.box.Box import Box
from package.app.client.modules.resignation.ResignationValidator import (
    ResignationValidator,
)
from package.app.client.state.ComponentState import ComponentState
from package.app.meta.Singleton import Singleton
from package.app.client.utils.form import getEntryBuffer
from package.app.api.modules.resignation.dto.ResignationDto import ResignationDto
from package.app.client.gui.imports import Gtk
from package.app.validation.IValidator import IValidator
from datetime import datetime


class ResignationComponent(metaclass=Singleton):
    def __init__(self):
        self.__state = ComponentState()
        self.__validator: IValidator = ResignationValidator()
        self.__controller = ResignationController()
        self.__dialogService = DialogService()

    def requestRegistration(self, selectedEmployeeId, selectedResignationTypeId, memoText) -> bool:

        memo = memoText
        selectedEmployee = self.getEmployeeById(
            selectedEmployeeId)
        selectedResignationType = self.getResignationTypeById(
            selectedResignationTypeId)

        try:
            dto = ResignationDto(
                employee_id=selectedEmployee.user_id,
                resignation_type_id=selectedResignationType.id,
                date = datetime.now(),
                memo = memo,
                employee = selectedEmployee,
                resignation_type = selectedResignationType,
            )
        except AttributeError:
            dto = ResignationDto(
                employee_id=None,
                resignation_type_id=None,
                date = None,
                memo = None,
                employee = None,
                resignation_type = None,
            )

        if self.__validator.execute(dto):
            entity = self.__controller.registerResignation(dto)
            if entity:
                self.__displaySuccessMessage()
            return True
        
        return False

    def getState(self) -> ComponentState:
        return self.__state

    def __displaySuccessMessage(self):
        content = Box()
        content.pack_default(Gtk.Label("A demiss??o foi corretamente executada!"))
        self.__dialogService.displayInfoBox(
            InfoBoxProps(title="Demiss??o executada", content=content)
        )

    def getEmployees(self):
        return self.__controller.getEmployees()

    def getResignationTypes(self):
        return self.__controller.getResignationTypes()

    def getEmployeeById(self, id):
        return self.__controller.getEmployeeById(id)

    def getResignationTypeById(self, resignationId):
        return self.__controller.getResignationTypeById(
            resignationId)

    def changeEmployeeRegisterStatus(self, id:int):
        return self.__controller.changeEmployeeRegisterStatus(id)
