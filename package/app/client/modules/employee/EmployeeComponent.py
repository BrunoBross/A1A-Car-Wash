from package.app.meta.Singleton import Singleton
from package.app.api.modules.user.UserService import UserService


class EmployeeComponent(metaclass=Singleton):
    def __init__(self):
        self.__userService = UserService()

    def getEmployeeFullNameByUsername(self, username: str):
        return self.__userService.getEmployeeFullNameByUsername(username)
