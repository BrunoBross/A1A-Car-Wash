from typing import Optional
from package.app.api.modules.resignation.dto.ResignationDto import ResignationDto
from package.app.meta.Singleton import Singleton
from package.app.api.modules.resignation.ResignationService import ResignationService


class ResignationController(metaclass=Singleton):
    def __init__(self):
        self.__resignationService = ResignationService()

    def registerResignation(self, resignation: ResignationDto) -> Optional[ResignationDto]:
        return self.__resignationService.registerResignation(resignation)
