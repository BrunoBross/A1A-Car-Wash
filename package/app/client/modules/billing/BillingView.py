from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk
from package.app.client.utils.markup import toBig
from package.app.client.gui.box.Box import Box
from package.app.client.modules.billing.BillingComponent import BillingComponent


class BillingView(metaclass=Singleton):
    def __init__(self):
        self.__component = BillingComponent()
        self.__month: Gtk.Widget

        self.__grossRevenueLabel = Gtk.Label()
        self.__netRevenueLabel = Gtk.Label()
        self.__employeeWagesLabel = Gtk.Label()
        self.__taxesLabel = Gtk.Label()

        self.__months = {
            "Selecione um mês": 0,
            "Janeiro": 1,
            "Fevereiro": 2,
            "Março": 3,
            "Abril": 4,
            "Maio": 5,
            "Junho": 6,
            "Julho": 7,
            "Agosto": 8,
            "Setembro": 9,
            "Outubro": 10,
            "Novembro": 11,
            "Dezembro": 12,
        }

        self.__grossRevenues = 0
        self.__netRevenues = 0
        self.__employeeWages = 0
        self.__taxes = 0

    def get(self) -> Gtk.Box:
        mainBox = Box(orientation=Gtk.Orientation.VERTICAL)

        monthSelectBox = Box(Gtk.Orientation.HORIZONTAL)
        monthSelectLabel = Gtk.Label()
        monthSelectLabel.set_markup(toBig("Mes:"))
        monthSelectComboBox = Gtk.ComboBoxText()
        monthSelectComboBox.set_entry_text_column(0)
        for month in self.__months:
            monthSelectComboBox.append_text(month)
        monthSelectComboBox.set_active(0)
        monthSelectBox.pack_default(monthSelectLabel)
        monthSelectBox.pack_default(monthSelectComboBox)

        monthSelectComboBox.connect("changed", self.getValues)

        monthSelectBox.set_margin_bottom(30)
        self.__grossRevenueLabel.set_margin_bottom(30)
        self.__employeeWagesLabel.set_margin_bottom(30)
        self.__taxesLabel.set_margin_bottom(30)
        self.__netRevenueLabel.set_margin_bottom(30)

        mainBox.pack_start(monthSelectBox, False, False, 0)
        mainBox.pack_start(self.__grossRevenueLabel, False, False, 0)
        mainBox.pack_start(self.__employeeWagesLabel, False, False, 0)
        mainBox.pack_start(self.__taxesLabel, False, False, 0)
        mainBox.pack_start(self.__netRevenueLabel, False, False, 0)

        return mainBox

    def getValues(self, _):
        if self.__months[_.get_active_text()] == 0:
            self.__grossRevenueLabel.set_markup("")
            self.__employeeWagesLabel.set_markup("")
            self.__taxesLabel.set_markup("")
            self.__netRevenueLabel.set_markup("")
            return

        values = self.__component.getBilling(self.__months[_.get_active_text()])

        self.__grossRevenues = values[0]
        self.__netRevenues = values[1]
        self.__employeeWages = values[2]
        self.__taxes = values[3]

        self.__grossRevenueLabel.set_markup(toBig(f"Faturamento Bruto: {self.__grossRevenues}"))
        self.__employeeWagesLabel.set_markup(toBig(f"Salário de Funcionários: {self.__employeeWages}"))
        self.__taxesLabel.set_markup(toBig(f"Impostos: {self.__taxes}"))
        self.__netRevenueLabel.set_markup(toBig(f"Faturamento Líquido: {self.__netRevenues}"))
