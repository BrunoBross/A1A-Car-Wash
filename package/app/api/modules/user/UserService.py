from typing import Optional
from package.app.api.modules.user.UserDtoMapper import UserDtoMapper
from package.app.api.modules.user.UserQuery import UserQuery
from package.app.api.modules.user.dto.UserDto import UserDto
from package.app.api.modules.user.dto.EmployeeDto import EmployeeDto
from package.app.meta.Singleton import Singleton
from colorama import Fore


class UserService(metaclass=Singleton):
    def __init__(self):
        self.__query = UserQuery()
        self.__userDtoMapper = UserDtoMapper()

    def getUserByUsername(self, username: str) -> Optional[UserDto]:
        user = self.__query.getUserByUsername(username)
        if user:
            return self.__userDtoMapper.mapUserToDto(user)
        return None

    def getEmployeeFullNameByUsername(self, username: str) -> Optional[EmployeeDto]:
        user = self.getUserByUsername(username)
        employee = self.__query.getEmployeeById(user.id)
        if employee:
            return employee.legal_name
        return None

    def createEmployee(self, username: str, fullname: str, password: str, salary: str):
        self.__query.createEmployee(username, fullname, password, salary)

