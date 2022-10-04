from typing import Optional
from package.app.api.model.User import User
from package.app.api.model.Employee import Employee
from package.app.api.orm.DAO import DAO
from package.app.meta.Singleton import Singleton
from package.app.api.enum.RoleEnum import RoleEnum


class UserQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()

    def getUserByUsername(self, username: str) -> Optional[User]:
        return self.__dao.select(User).where(User.username == username).first()

    def getEmployeeById(self, user_id: int) -> Optional[Employee]:
        return self.__dao.select(Employee).where(Employee.user_id == user_id).first()

    def createEmployee(self, username: str, fullname: str, password: str, salary: str):
        self.__dao.insert(User(username=username, password=password, role_id=RoleEnum.FUNCIONARIO.value))
        userId = self.__dao.select(User).where(User.username == username).first().id
        self.__dao.insert(Employee(user_id=userId, legal_name=fullname, wage=salary, active_register=True))
