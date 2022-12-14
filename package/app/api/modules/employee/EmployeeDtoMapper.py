from package.app.api.model.Employee import Employee
from package.app.api.modules.employee.dto.EmployeeDto import EmployeeDto
from package.app.api.modules.user.UserDtoMapper import UserDtoMapper
from package.app.meta.Singleton import Singleton


class EmployeeDtoMapper(metaclass=Singleton):
    def __init__(self):
        self.__userDtoMapper = UserDtoMapper()

    def mapEmployeeToDto(self, employee: Employee) -> EmployeeDto:
        return EmployeeDto(
            id=employee.id,
            user=self.__userDtoMapper.mapUserToDto(employee.user),
            legalName=employee.legal_name,
            wage=employee.wage,
            activeRegister=employee.active_register,
            jobLimit=str(employee.job_limit),
            admission_date=employee.admission_date,
        )

    def mapDtoToEmployee(self, dto: EmployeeDto) -> Employee:
        return Employee(
            user_id=dto.user.id,
            legal_name=dto.legalName,
            wage=dto.wage,
            job_limit=dto.jobLimit,
        )
