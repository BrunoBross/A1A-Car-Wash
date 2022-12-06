from package.app.api.modules.generalreport.generalReportService import GeneralReportService
from package.app.meta.Singleton import Singleton
from datetime import datetime
from package.app.api.modules.generalreport.generalReportValidator import GeneralReportValidator

class GeneralReportController(metaclass=Singleton):
    def __init__(self):
        self.__employeeReportService = GeneralReportService()
        self.__employeeReportValidator = GeneralReportValidator()