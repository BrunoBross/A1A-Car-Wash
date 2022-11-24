from package.app.api.modules.warning.WarningQuery import WarningQuery
from package.app.meta.Singleton import Singleton


class WarningService(metaclass=Singleton):
    def __init__(self):
        self.__query = WarningQuery()

    def getWarningList(self, employee_id: int):
        return self.__query.getWarningList(employee_id)

    def changeWarningReadStatus(self, warning_id: int, read_bool: bool):
        self.__query.updateWarningReadStatus(warning_id, read_bool)

    def deleteWarningByEmployeeId(self, employee_id: int):
        self.__query.deleteWarningByEmployeeId(employee_id)
