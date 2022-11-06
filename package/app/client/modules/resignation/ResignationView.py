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
        self.__employeeCombo = Gtk.Widget
        self.__resignationTypeCombo = Gtk.Widget
        self.__memoInput = Gtk.Widget

    def get(self) -> Gtk.Box:

        mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)


        # MAIN LABEL  
        label = Gtk.Label()
        label.set_markup(toBig("Demitir Funcionário"))
        label.set_margin_bottom(30)


        # EMPLOYEE BOX
        employeeBox = Box(Gtk.Orientation.HORIZONTAL)
        employeeBox.set_margin_bottom(5)
        employeeBox.set_margin_top(5)
        
        employeeLabel = Gtk.Label()
        employeeLabel.set_markup("Funcionário*:")
        employeeBox.pack_default(employeeLabel)
        
        employeeCombo = Gtk.ComboBoxText()
        employeeCombo.set_entry_text_column(0)
        employeeCombo.append_text("Selecione um funcionário")
        employeeCombo.append_text("Selecione outro funcionário")
        employeeCombo.set_active(0)
        employeeCombo.set_size_request(275,30)
        employeeBox.pack_default(employeeCombo)
        

        # RESIGNATION TYPE BOX
        resignationTypeBox = Box(Gtk.Orientation.HORIZONTAL)
        resignationTypeBox.set_margin_bottom(5)
        resignationTypeBox.set_margin_top(5)

        resignationTypeLabel = Gtk.Label()
        resignationTypeLabel.set_markup("Tipo de causa*:")
        resignationTypeBox.pack_default(resignationTypeLabel)
        
        resignationTypeCombo = Gtk.ComboBoxText()
        resignationTypeCombo.set_entry_text_column(0)
        resignationTypeCombo.append_text("Selecione uma causa")
        resignationTypeCombo.append_text("Selecione outra causa")
        resignationTypeCombo.set_active(0)
        resignationTypeCombo.set_size_request(285,30)
        resignationTypeBox.pack_default(resignationTypeCombo)


        # MEMO BOX
        memoBox = Box(Gtk.Orientation.HORIZONTAL)
        memoBox.set_margin_top(5)
        memoBox.set_margin_bottom(5)
       
        memoLabel = Gtk.Label()
        memoLabel.set_text("Observação:")
        
        memoBox.pack_default(memoLabel)
        memoInput = Gtk.Entry()
        memoInput.set_size_request(268,90)
        memoBox.pack_default(memoInput)


        # BUTTONS BOX
        ButtonsBox = Box(Gtk.Orientation.HORIZONTAL)
        ButtonsBox.set_margin_top(30)

        goBackButton = Gtk.Button(label="Voltar")
        goBackButton.set_margin_right(15)
        goBackButton.set_size_request(100,30)
        ButtonsBox.pack_default(goBackButton)

        confirmButton = Gtk.Button(label="Cadastrar")
        confirmButton.set_margin_left(15)
        confirmButton.set_size_request(100,30)
        confirmButton.connect("clicked", self.__onConfirm)
        ButtonsBox.pack_default(confirmButton)


        self.__employeeCombo = employeeCombo
        self.__resignationTypeCombo = resignationTypeCombo
        self.__memoInput = memoInput

        mainBox.pack_start(label, False, False, 0)
        mainBox.pack_start(employeeBox, False, False, 0)
        mainBox.pack_start(resignationTypeBox, False, False, 0)
        mainBox.pack_start(memoBox, False, False, 0)
        mainBox.pack_start(ButtonsBox, False, False, 0)

        return mainBox

    def __onConfirm(self, _: Gtk.Widget):
        self.__component.getState().addReference("employee", self.__employeeCombo)
        self.__component.getState().addReference("resignationType", self.__resignationTypeCombo)
        self.__component.getState().addReference("memo", self.__memoInput)

        self.__component.requestRegistration()

    def getEmployees():
        pass
