from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.api.modules.employee.dto.EmployeeDto import EmployeeDto
from package.app.client.modules.registeremployee.RegisterEmployeeValidator import (
    RegisterEmployeeValidator,
)
from package.app.meta.Singleton import Singleton
from package.app.api.modules.employee.EmployeeController import EmployeeController
from package.app.client.state.ComponentState import ComponentState
from package.app.client.utils.form import getEntryBuffer


class RegisterEmployeeComponent(metaclass=Singleton):
    def __init__(self):
        self.__employeeController = EmployeeController()
        self.__state = ComponentState()
        self.__validator = RegisterEmployeeValidator()

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
            self.__employeeController.registerEmployee(
                employeeDto=employeeDto, authDto=authDto
            )

    def getState(self) -> ComponentState:
        return self.__state
