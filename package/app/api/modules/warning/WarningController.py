from typing import Optional
from package.app.api.modules.warning.WarningService import WarningService
from package.app.api.modules.warning.dto.WarningDto import WarningDto
from package.app.decorators import post_endpoint
from package.app.meta.Singleton import Singleton


class WarningController(metaclass=Singleton):
    def __init__(self) -> None:
        self.__service = WarningService()

    def getWarnings(self):
        return self.__service.getWarnings()

    @post_endpoint
    def registerWarning(self, warningDto: WarningDto) -> Optional[WarningDto]:
        return self.__service.registerWarning(warningDto)

    @post_endpoint
    def editWarning(self, warningDto: WarningDto, warningId: int):
        self.__service.editWarning(warningDto, warningId)

    @post_endpoint
    def deleteWarning(self, warningId: int):
        self.__service.deleteWarning(warningId)
