from datetime import date
from typing import List
from package.app.api.model.Warning import Warning
from package.app.api.model.WarningTable import WarningTable
from package.app.api.orm.DAO import DAO
from package.app.meta.Singleton import Singleton


class WarningQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()

    def getWarningList(self, employee_id: int) -> List[WarningTable]:
        return self.__dao.select(WarningTable)\
            .join(Warning, WarningTable.warning_id == Warning.id)\
            .where(WarningTable.employee_id == employee_id)\
            .where(Warning.date == date.today())\
            .all()
