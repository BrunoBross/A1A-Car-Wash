from typing import List
from datetime import date
from package.app.api.model.Warning import Warning
from package.app.api.orm.DAO import DAO
from package.app.meta.Singleton import Singleton


class WarningQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()

    def getWarningList(self) -> List[Warning]:
        return self.__dao.select(Warning).where(Warning.date == date.today()).all()
