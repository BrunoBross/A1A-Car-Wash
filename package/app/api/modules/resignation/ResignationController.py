from typing import Optional
from package.app.api.modules.resignation.dto.ResignationDto import ResignationDto
from package.app.meta.Singleton import Singleton
from package.app.api.modules.resignation.ResignationService import ResignationService


class ResignationController(metaclass=Singleton):
    def __init__(self):
        self.__resignationService = ResignationService()

    def registerResignation(self, resignation: ResignationDto) -> Optional[ResignationDto]:
        return self.__resignationService.registerResignation(resignation)

    def getEmployees(self):
        return self.__resignationService.getEmployees()

    def getResignationTypes(self):
        return self.__resignationService.getResignationTypes()

    def getEmployeeById(self, id):
        return self.__resignationService.getEmployeeById(id)

    def getResignationTypeById(self, resignationId):
        return self.__resignationService.getResignationTypeById(
            resignationId)
        
    def changeEmployeeRegisterStatus(self, id:int):
        return self.__resignationService.changeEmployeeRegisterStatus(id)
