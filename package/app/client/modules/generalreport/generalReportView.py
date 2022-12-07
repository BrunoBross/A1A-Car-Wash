from package.app.client.modules.generalreport.generalReportComponent import GeneralReportComponent
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk
from package.app.client.utils.markup import toBig
from package.app.client.gui.box.Box import Box
import re

class GeneralReportView(metaclass=Singleton):
    def __init__(self):
        self.__component = GeneralReportComponent()
        self.__selectedMonth = ""
        self.__months = {
            "Selecione um mês": 0,
            "Janeiro": "01",
            "Fevereiro": "02",
            "Março": "03",
            "Abril": "04",
            "Maio": "05",
            "Junho": "06",
            "Julho": "07",
            "Agosto": "08",
            "Setembro": "09",
            "Outubro": "10",
            "Novembro": "11",
            "Dezembro": "12",
        }

    def get(self) -> Gtk.Box:
        mainBox = Box(orientation=Gtk.Orientation.VERTICAL)
        title = Gtk.Label()
        title.set_markup(toBig("Emitir Relatório Geral"))
        title.set_margin_bottom(30)
        mainBox.pack_start(title, False, False, 0)

        #ComboBox de Meses
        comboMesesBox = Box(Gtk.Orientation.HORIZONTAL)
        comboMesesSelectLabel = Gtk.Label()
        comboMesesSelectLabel.set_markup(toBig("Selecione um mês:"))
        comboMesesSelectComboBox = Gtk.ComboBoxText()
        comboMesesSelectComboBox.set_entry_text_column(0)
        for month in self.__months:
            comboMesesSelectComboBox.append_text(month)
        comboMesesSelectComboBox.set_active(0)
        comboMesesSelectComboBox.connect("changed", self.updateSelectedMonth)
        comboMesesBox.pack_default(comboMesesSelectLabel)
        comboMesesBox.pack_default(comboMesesSelectComboBox)

        #Botao de comfirmar
        confirmButton = Gtk.Button(label="Emitir Relatório")
        confirmButton.set_margin_top(30)
        confirmButton.connect("clicked", self.onConfirm)

        mainBox.pack_start(comboMesesBox, False, False, 0)
        mainBox.pack_start(confirmButton, False, False, 0)

        return mainBox

    def onConfirm(self, _):
        self.__component.getGeneralReport(self.__selectedMonth)

    def updateSelectedMonth(self, _):
        selectedMonthText = _.get_active_text()
        self.__selectedMonth = self.__months[selectedMonthText]
        