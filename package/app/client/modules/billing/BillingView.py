from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk
from package.app.client.utils.markup import toBig
from package.app.client.gui.box.Box import Box
from package.app.client.modules.billing.BillingComponent import BillingComponent


class BillingView(metaclass=Singleton):
    def __init__(self):
        self.__component = BillingComponent()
        self.__month: Gtk.Widget

    def get(self) -> Gtk.Box:
        mainBox = Box(orientation=Gtk.Orientation.VERTICAL)

        monthSelectBox = Box(Gtk.Orientation.HORIZONTAL)
        monthSelectLabel = Gtk.Label()
        monthSelectLabel.set_markup(toBig("Mes:"))
        monthSelectComboBox = Gtk.ComboBoxText()
        monthSelectComboBox.set_entry_text_column(0)
        for i in range(1, 13):
            monthSelectComboBox.append_text(str(i))
        monthSelectComboBox.set_active(0)
        monthSelectBox.pack_default(monthSelectLabel)
        monthSelectBox.pack_default(monthSelectComboBox)

        grossRevenue = Gtk.Label()
        netRevenue = Gtk.Label()
        employeeWages = Gtk.Label()
        taxes = Gtk.Label()

        grossRevenue.set_markup(toBig(f"Faturamento Bruto: {self.__component.getGrossRevenue()}"))
        netRevenue.set_markup(toBig(f"Faturamento Líquido: {self.__component.getNetRevenue()}"))
        employeeWages.set_markup(toBig(f"Salário de Funcionários: {self.__component.getEmployeeWages()}"))
        taxes.set_markup(toBig(f"Impostos: {self.__component.getTaxes()}"))

        monthSelectBox.set_margin_bottom(30)
        grossRevenue.set_margin_bottom(30)
        netRevenue.set_margin_bottom(30)
        employeeWages.set_margin_bottom(30)
        taxes.set_margin_bottom(30)

        mainBox.pack_start(monthSelectBox, False, False, 0)
        mainBox.pack_start(grossRevenue, False, False, 0)
        mainBox.pack_start(netRevenue, False, False, 0)
        mainBox.pack_start(employeeWages, False, False, 0)
        mainBox.pack_start(taxes, False, False, 0)

        return mainBox
