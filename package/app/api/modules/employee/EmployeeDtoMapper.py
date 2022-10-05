from package.app.api.model.Employee import Employee
from package.app.api.modules.user.dto.EmployeeDto import EmployeeDto
from package.app.meta.Singleton import Singleton


class EmployeeDtoMapper(metaclass=Singleton):
    def __init__(self):
        pass

    def mapEmployeeToDto(self, employee: Employee) -> EmployeeDto:
        return EmployeeDto(id=employee.id, legal_name=employee.legal_name, wage=employee.wage, active_register=employee.active_register)
