from package.app.meta.Singleton import Singleton
from package.app.api.modules.employee.EmployeeController import EmployeeController
from package.app.api.modules.billing.BillingController import BillingController
from package.app.api.modules.generalreport.generalReportController import GeneralReportController
from package.app.client.dialog.DialogService import DialogService
from package.app.client.gui.box.Box import Box
from package.app.client.gui.imports import Gtk
from package.app.client.dialog.InfoBox import InfoBoxProps
import csv
from pathlib import Path

class GeneralReportComponent(metaclass=Singleton):
    def __init__(self):
        self.__employeeController = EmployeeController()
        self.__billingController = BillingController()
        self.__generalReportController = GeneralReportController()
        self.__dialogService = DialogService()