from typing import List, Optional
from package.app.api.model.Employee import Employee
from package.app.api.orm.DAO import DAO
from package.app.exception.DatabaseIntegrityException import DatabaseIntegrityException
from package.app.meta.Singleton import Singleton


class EmployeeQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()

    def getEmployees(self) -> List[Employee]:
        return self.__dao.select(Employee).all()

    def getEmployeeByUserId(self, user_id: int) -> Optional[Employee]:
        return self.__dao.select(Employee).where(Employee.user_id == user_id).first()

    def registerEmployee(self, employee: Employee):
        try:
            self.__dao.insert(employee)
            return employee
        except DatabaseIntegrityException:
            return None
