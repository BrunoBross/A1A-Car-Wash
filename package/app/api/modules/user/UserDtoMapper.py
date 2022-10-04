from package.app.api.enum.RoleEnum import RoleEnum
from package.app.api.model.User import User
from package.app.api.model.Employee import Employee
from package.app.api.modules.user.dto.UserDto import UserDto
from package.app.api.modules.user.dto.EmployeeDto import EmployeeDto
from package.app.meta.Singleton import Singleton


class UserDtoMapper(metaclass=Singleton):
    def __init__(self):
        pass

    def mapUserToDto(self, user: User) -> UserDto:
        return UserDto(id=user.id, username=user.username, role=RoleEnum(user.role.id))

    def mapEmployeeToDto(self, employee: Employee) -> EmployeeDto:
        return EmployeeDto(id=employee.id, legal_name=employee.legal_name, wage=employee.wage, active_register=employee.active_register)
