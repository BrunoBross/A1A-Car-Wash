from package.app.client.modules.employeeReport.employeeReportComponent import EmployeeReportComponent
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk
from package.app.client.utils.markup import toBig
from package.app.client.gui.box.Box import Box

class EmployeeReportView(metaclass=Singleton):
    def __init__(self):
        self.__component = EmployeeReportComponent()
        self.__employees = self.__component.getEmployees()
        
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
        title.set_markup(toBig("Agendamentos"))
        title.set_margin_bottom(30)
        mainBox.pack_start(title, False, False, 0)

        #ComboBox de employees
        comboEmployeeBox = Box(Gtk.Orientation.HORIZONTAL)
        comboEmployeeBox.set_margin_bottom(5)
        comboEmployeeBox.set_margin_top(5)
        #comboEmployeeBoxSelectLabel = Gtk.Label()
        comboEmployeeLabel = Gtk.Label()
        comboEmployeeLabel.set_markup(toBig("Funcionário*"))
        comboEmployeeBox.pack_default(comboEmployeeLabel)
        
        employeeCombo = Gtk.ComboBoxText()
        employeeCombo.set_entry_text_column(0)
        employeeCombo.append_text("0 - Escolha um funcionário")
        for employee in self.__employees:
            employeeCombo.append_text(
                f"{employee.id}" + " - " + f"{employee.legalName[0:28]}")
        
        comboEmployeeBox.pack_default(employeeCombo)


        #ComboBox de Meses
        comboMesesBox = Box(Gtk.Orientation.HORIZONTAL)
        comboMesesSelectLabel = Gtk.Label()
        comboMesesSelectLabel.set_markup(toBig("Selecione um mês:"))
        comboMesesSelectComboBox = Gtk.ComboBoxText()
        comboMesesSelectComboBox.set_entry_text_column(0)
        for month in self.__months:
            comboMesesSelectComboBox.append_text(month)
        comboMesesSelectComboBox.set_active(0)
        comboMesesBox.pack_default(comboMesesSelectLabel)
        comboMesesBox.pack_default(comboMesesSelectComboBox)
        #Botao de comfirmar
        confirmButton = Gtk.Button(label="Emitir Relatorio")
        confirmButton.set_margin_top(30)
        #packStarts
        mainBox.pack_start(comboEmployeeBox, False, False, 0)
        mainBox.pack_start(comboMesesBox, False, False, 0)
        mainBox.pack_start(confirmButton, False, False, 0)
        #o que falta
        #fazer as coisas da view
        #fazer funcs no component
        #pegar os dados
        #gerar o CSV

        return mainBox


    
