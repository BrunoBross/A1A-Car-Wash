from package.app.api.modules.warning.WarningQuery import WarningQuery
from package.app.api.modules.warning.dto.WarningDto import WarningDto
from package.app.meta.Singleton import Singleton


class WarningService(metaclass=Singleton):
    def __init__(self):
        self.__query = WarningQuery()

    def registerWarning(self, warningDto: WarningDto):
        return self.__query.registerWarning(warningDto)

    def editWarning(self, warningDto: WarningDto, warningId: int):
        self.__query.updateWarning(warningId, warningDto)

    def deleteWarning(self, warningId: int):
        self.__query.deleteWarning(warningId)

    def getWarnings(self):
        return self.__query.getWarnings()

    def getWarningList(self, employee_id: int):
        return self.__query.getWarningList(employee_id)

    def changeWarningReadStatus(self, warning_id: int, read_bool: bool):
        self.__query.updateWarningReadStatus(warning_id, read_bool)

    def deleteWarningByEmployeeId(self, employee_id: int):
        self.__query.deleteWarningByEmployeeId(employee_id)
