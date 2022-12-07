from datetime import date, datetime
from typing import List
from package.app.api.model.Warning import Warning
from package.app.api.model.WarningTable import WarningTable
from package.app.api.modules.employee.EmployeeQuery import EmployeeQuery
from package.app.api.modules.warning.dto.WarningDto import WarningDto
from package.app.api.orm.DAO import DAO
from package.app.meta.Singleton import Singleton
from package.app import sqlalchemy_session


class WarningQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()
        self.__session = sqlalchemy_session
        self.__employeeQuery = EmployeeQuery()

    def registerWarning(self, warningDto: WarningDto):
        try:
            self.__dao.insert(
                Warning(
                    description=warningDto.description,
                    date=datetime.strptime(warningDto.date, "%Y-%m-%d").date(),
                )
            )
        except:
            return None
        warning = self.__dao.select(Warning).order_by(Warning.id.desc()).first()
        employees = self.__employeeQuery.getEmployees()
        for employee in employees:
            self.__dao.insert(
                WarningTable(employee_id=employee.id, warning_id=warning.id)
            )
        return warning

    def deleteWarning(self, warningId: int):
        return self.__dao.delete(self.__dao.get(Warning, warningId))

    def updateWarning(self, warningId: int, warningDto: WarningDto):
        print(warningId)
        self.__dao.update(
            Warning, (Warning.id == warningId), "description", warningDto.description
        )

    def getWarnings(self):
        return self.__dao.select(Warning).all()

    def getWarningList(self, employee_id: int) -> List[WarningTable]:
        return (
            self.__dao.select(WarningTable)
            .join(Warning, WarningTable.warning_id == Warning.id)
            .where(WarningTable.employee_id == employee_id)
            .where(Warning.date == date.today())
            .all()
        )

    def updateWarningReadStatus(self, warning_id: int, read_bool: bool):
        self.__session.query(WarningTable).where(WarningTable.id == warning_id).update(
            {"read": read_bool}
        )

        self.__session.commit()

    def deleteWarningByEmployeeId(self, employee_id: int):
        warning_list = (
            self.__dao.select(WarningTable)
            .where(WarningTable.employee_id == employee_id)
            .all()
        )
        for warning in warning_list:
            self.__dao.delete(warning)
