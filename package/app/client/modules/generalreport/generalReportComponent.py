from package.app.meta.Singleton import Singleton
from package.app.api.modules.employee.EmployeeController import EmployeeController
from package.app.api.modules.billing.BillingController import BillingController
from package.app.api.modules.generalreport.generalReportController import GeneralReportController
from package.app.client.dialog.DialogService import DialogService
from package.app.client.modules.generalreport.generalReportValidator import GeneralReportValidator
from package.app.client.gui.box.Box import Box
from package.app.client.gui.imports import Gtk
from package.app.client.dialog.InfoBox import InfoBoxProps
import csv
from pathlib import Path
from datetime import datetime

class GeneralReportComponent(metaclass=Singleton):
    def __init__(self):
        self.__generalReportController = GeneralReportController()
        self.__dialogService = DialogService()
        self.__validator = GeneralReportValidator()

    def getGeneralReport(self, month:str):
        if self.__validator.execute(month):
            downloads_path = str(Path.home() / "Downloads")
            reportDataHeader = ["Veículos atendidos", "Serviços realizados", "Funcionários", "Ausências de clientes"]
            reportDataList = self.__generalReportController.getGeneralReport(month)
            data = str(datetime.now())
            with open(f"{downloads_path}/relatorio_geral_{data[0:10]}_{data[11:19]}.csv", 'w') as csvFile:
                csv.writer(csvFile, delimiter=',').writerow(reportDataHeader)
                csv.writer(csvFile, delimiter=',').writerow(reportDataList)
            self.__displaySuccessMessage()

    def __displaySuccessMessage(self):
        content = Box()
        content.pack_default(Gtk.Label("Relatorio emitido com sucesso!"))
        self.__dialogService.displayInfoBox(
            InfoBoxProps(title="Relatorio emitido!", content=content)
        )
        