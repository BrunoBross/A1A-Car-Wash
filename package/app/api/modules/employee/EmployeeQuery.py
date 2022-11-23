from typing import List, Optional
from package.app.api.model.Employee import Employee
from package.app.api.orm.DAO import DAO
from package.app.exception.DatabaseIntegrityException import DatabaseIntegrityException
from package.app.meta.Singleton import Singleton
from package.app import sqlalchemy_session
from sqlalchemy import delete


class EmployeeQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()
        self.__session = sqlalchemy_session

    def getEmployee(self, id: int) -> Optional[Employee]:
        return self.__dao.get(Employee, id)

    def getEmployees(self) -> List[Employee]:
        return self.__dao.select(Employee).all()

    def getEmployeeByUserId(self, user_id: int) -> Optional[Employee]:
        return self.__dao.select(Employee).where(Employee.user_id == user_id).first()

    def getEmployeeById(self, id: int) -> Optional[Employee]:
        return self.__dao.select(Employee).where(Employee.id == id).first()

    def registerEmployee(self, employee: Employee):
        try:
            self.__dao.insert(employee)
            return employee
        except DatabaseIntegrityException:
            return None

    def updateEmployee(self, employeeUpdates: list, user_id: int):
        for update in employeeUpdates:
            self.__session.query(Employee)\
                .where(Employee.user_id == user_id)\
                .update(update)

            self.__session.commit()

    def deleteEmployee(self, user_id: int):
        self.__dao.select(Employee).where(Employee.user_id == user_id).delete()

