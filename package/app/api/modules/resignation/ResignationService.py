from typing import Optional
from package.app.api.modules.resignation.ResignationDtoMapper import ResignationDtoMapper
from package.app.api.modules.resignation.dto.ResignationDto import ResignationDto
from package.app.meta.Singleton import Singleton
from package.app.api.modules.resignation.ResignationQuery import ResignationQuery


class ResignationService(metaclass=Singleton):
    def __init__(self):
        self.__query = ResignationQuery()
        self.__mapper = ResignationDtoMapper()

    def registerResignation(self, resignationDto: ResignationDto) -> Optional[ResignationDto]:
        self.__query.registerResignation(self.__mapper.mapDtoToResignation(resignationDto))
        return resignationDto
        
    def getEmployees(self):
        return self.__query.getEmployees()

    def getResignationTypes(self):
        return self.__query.getResignationTypes()

    def getEmployeeById(self, id):
        return self.__query.getEmployeeById(id)

    def getResignationTypeById(self, ResignationId):
        return self.__query.getResignationTypeById(ResignationId)

    def changeEmployeeRegisterStatus(self, id:int):
        return self.__query.changeEmployeeRegisterStatus(id)

    def deleteResignationByEmployeeId(self, employee_id):
        self.__query.deleteResignationByEmployeeId(employee_id)
