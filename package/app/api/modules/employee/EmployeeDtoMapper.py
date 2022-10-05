from package.app.api.model.Employee import Employee
from package.app.api.modules.employee.dto.EmployeeDto import EmployeeDto
from package.app.meta.Singleton import Singleton


class EmployeeDtoMapper(metaclass=Singleton):
    def mapEmployeeToDto(self, employee: Employee) -> EmployeeDto:
        return EmployeeDto(
            id=employee.id,
            legalName=employee.legal_name,
            wage=employee.wage,
            activeRegister=employee.active_register,
        )
