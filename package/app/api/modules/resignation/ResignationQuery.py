from typing import Optional
from package.app.api.model.Resignation import Resignation
from package.app.exception.DatabaseIntegrityException import DatabaseIntegrityException
from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO
from package.app.api.model.Employee import Employee
from package.app.api.model.ResignationType import ResignationType


class ResignationQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()

    def registerResignation(self, resignation: Resignation) -> Optional[Resignation]:
        try:
            self.__dao.insert(resignation)
            return resignation
        except DatabaseIntegrityException:
            return None

    def getEmployees(self):
        return self.__dao.select(Employee).where(Employee.active_register==True).all()

    def getResignationTypes(self):
        return self.__dao.select(ResignationType).all()

    def getEmployeeById(self, id: int):
        try:
            return self.__dao.select(Employee).where(Employee.id == id).all()[0]
        except IndexError:
            return None

    def getResignationTypeById(self, resignationTypeId: int):
        try:
            return self.__dao.select(ResignationType).where(
                ResignationType.id == resignationTypeId).all()[0]
        except IndexError:
            return None

    def getResignatedEmployeeAfterDateId(self, date):
        return self.__dao.select(Resignation.employee_id) \
            .where(Resignation.date > date) \
            .all()

    def changeEmployeeRegisterStatus(self, id:int):
        try:
            self.__dao.update(Employee, (Employee.id == id), "active_register", False)
            return None
        except DatabaseIntegrityException:
            return None

    def deleteResignationByEmployeeId(self, employee_id):
        try:
            self.__dao.delete(self.__dao.select(Resignation).where(Resignation.employee_id == employee_id).first())
        except DatabaseIntegrityException:
            return None
