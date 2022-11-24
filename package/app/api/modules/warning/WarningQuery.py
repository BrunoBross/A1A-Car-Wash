from datetime import date
from typing import List
from package.app.api.model.Warning import Warning
from package.app.api.model.WarningTable import WarningTable
from package.app.api.orm.DAO import DAO
from package.app.meta.Singleton import Singleton
from package.app import sqlalchemy_session


class WarningQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()
        self.__session = sqlalchemy_session

    def getWarningList(self, employee_id: int) -> List[WarningTable]:
        return self.__dao.select(WarningTable)\
            .join(Warning, WarningTable.warning_id == Warning.id)\
            .where(WarningTable.employee_id == employee_id)\
            .where(Warning.date == date.today())\
            .all()

    def updateWarningReadStatus(self, warning_id: int, read_bool: bool):
        self.__session.query(WarningTable)\
            .where(WarningTable.id == warning_id)\
            .update({"read": read_bool})

        self.__session.commit()
