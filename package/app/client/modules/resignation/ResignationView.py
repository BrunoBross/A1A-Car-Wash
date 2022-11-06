from package.app.client.modules.resignation.ResignationComponent import (
    ResignationComponent,
)
from package.app.meta.Singleton import Singleton
from package.app.client.utils.markup import toBig
from package.app.client.gui.box.Box import Box
from package.app.client.gui.imports import Gtk


class ResignationView(metaclass=Singleton):
    def __init__(self):
        self.__component = ResignationComponent()
        self.__EmployeeCombo = Gtk.Widget
        self.__ResignationTypeCombo = Gtk.Widget

    def get(self) -> Gtk.Box:

        mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        label = Gtk.Label()
        label.set_markup(toBig("Demitir Funcionário"))
        label.set_margin_bottom(30)



        employeeBox = Box(Gtk.Orientation.HORIZONTAL)
        
        employeeLabel = Gtk.Label()
        employeeLabel.set_markup("Funcionário*:")
        employeeBox.pack_default(employeeLabel)
        
        employeeCombo = Gtk.ComboBoxText()
        employeeCombo.set_entry_text_column(0)
        employeeCombo.append_text("Selecione um funcionário")
        employeeCombo.append_text("Selecione um funcionário2")
        employeeCombo.set_active(0)
        employeeCombo.new()
        employeeBox.pack_default(employeeCombo)
        


        jobValueBox = Box(Gtk.Orientation.HORIZONTAL)
       
        jobValueLabel = Gtk.Label()
        jobValueLabel.set_text("Preço do serviço*")
        jobValueLabel.set_margin_top(5)
        jobValueLabel.set_margin_left(5)
        jobValueLabel.set_margin_bottom(5)
        jobValueLabel.set_margin_right(5)
        
        jobValueBox.pack_default(jobValueLabel)
        jobValueInput = Gtk.Entry()
        jobValueInput.set_margin_top(5)
        jobValueInput.set_margin_left(5)
        jobValueInput.set_margin_bottom(5)
        jobValueInput.set_margin_right(5)
        jobValueBox.pack_default(jobValueInput)

        confirmButton = Gtk.Button(label="Cadastrar")
        confirmButton.set_margin_top(30)
        confirmButton.connect("clicked", self.__onConfirm)

        self.__EmployeeCombo = employeeCombo
        self.__jobValueInput = jobValueInput

        mainBox.pack_start(label, False, False, 0)
        mainBox.pack_start(employeeBox, False, False, 0)
        mainBox.pack_start(jobValueBox, False, False, 0)
        mainBox.pack_start(confirmButton, False, False, 0)

        return mainBox

    def __onConfirm(self, _: Gtk.Widget):
        self.__component.getState().addReference("jobName", self.__EmployeeCombo)
        self.__component.getState().addReference("jobValue", self.__ResignationTypeCombo)

        self.__component.requestRegistration()

    def getEmployees():
        pass
