from package.app.api.modules.employee.EmployeeController import EmployeeController
from package.app.meta.Singleton import Singleton
from package.app.api.modules.billing.BillingController import BillingController
from package.app.api.modules.employeeReport.employeeReportController import EmployeeReportController
from package.app.client.dialog.DialogService import DialogService
from package.app.client.gui.box.Box import Box
from package.app.client.gui.imports import Gtk
from package.app.client.dialog.InfoBox import InfoBoxProps
import csv
from pathlib import Path

class EmployeeReportComponent(metaclass=Singleton):
    def __init__(self):
        self.__employeeController = EmployeeController()
        self.__billingController = BillingController()
        self.__employeeReportController = EmployeeReportController()
        self.__dialogService = DialogService()
        

    def getEmployees(self):
        return self.__employeeController.getEmployees()

    def getStartMonthFormat(self, month):
        return self.__employeeReportController.getStartMonthFormat(month)

    def getEmployeeReport(self, employeeID:int, month:str):
        #return self.__employeeReportController.getEmployeeReport(employeeID, month)
        downloads_path = str(Path.home() / "Downloads")
        print(downloads_path)
        reportDataHeader = ["Nome", "Valor total de agendamentos", "Salario Bruto", "Salario Liquido", "Total de comissoes", "Total de penalidades"]
        reportDataList = self.__employeeReportController.getEmployeeReport(employeeID, month)
        print("------------------------------------")
        print(reportDataList)
        print("----------------------------------")
        with open( downloads_path + "/"+ 'relatorio_funcionario'+reportDataList[0]+"_"+month+"_"+'.csv', 'w') as csvFile:
            csv.writer(csvFile, delimiter=',').writerow(reportDataHeader)
            csv.writer(csvFile, delimiter=',').writerow(reportDataList)
        self.__displaySuccessMessage()

    def __displaySuccessMessage(self):
        content = Box()
        content.pack_default(Gtk.Label("Relatorio emitido com sucesso!"))
        self.__dialogService.displayInfoBox(
            InfoBoxProps(title="Relatorio emitido!", content=content)
        )
