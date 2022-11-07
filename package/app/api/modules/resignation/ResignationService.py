from typing import Optional
from package.app.api.modules.resignation.ResignationDtoMapper import ResignationDtoMapper
from package.app.api.modules.resignation.ResignationValidator import ResignationValidator
from package.app.api.modules.resignation.dto.ResignationDto import ResignationDto
from package.app.meta.Singleton import Singleton
from package.app.api.modules.resignation.ResignationQuery import ResignationQuery
from package.app.validation.IValidator import IValidator


class ResignationService(metaclass=Singleton):
    def __init__(self):
        self.__query = ResignationQuery()
        self.__mapper = ResignationDtoMapper()
        self.__validator: IValidator = ResignationValidator()

    def registerResignation(self, resignationDto: ResignationDto) -> Optional[ResignationDto]:
        if self.__validator.execute(resignationDto):
            self.__query.registerResignation(self.__mapper.mapDtoToResignation(resignationDto))
            return resignationDto
        return None

    def getEmployees(self):
        return self.__query.getEmployees()

    def getResignationTypes(self):
        return self.__query.getResignationTypes()
