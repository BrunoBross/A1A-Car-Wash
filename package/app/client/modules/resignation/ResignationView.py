from package.app.client.modules.resignation.ResignationComponent import (
    ResignationComponent,
)
from package.app.meta.Singleton import Singleton
from package.app.client.utils.markup import toBig
from package.app.client.gui.box.Box import Box
from package.app.client.gui.imports import Gtk
import re

class ResignationView(metaclass=Singleton):
    
    def __init__(self):
        self.__component = ResignationComponent()

        self.__employeeCombo = Gtk.ComboBoxText
        self.__resignationTypeCombo = Gtk.ComboBoxText
        self.__memoInput = Gtk.Entry

        self.__employees = list
        self.__resignationTypes = list

        self.__selectedEmployeeId = int 
        self.__selectedResignationTypeId = int
        self.__memo = str


    def get(self) -> Gtk.Box:
        self.getData()
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
        employeeLabel.set_markup("Funcionário*")
        employeeBox.pack_default(employeeLabel)
        
        employeeCombo = Gtk.ComboBoxText()
        employeeCombo.set_entry_text_column(0)
        self.fillEmployeeCombo(employeeCombo)
        employeeCombo.set_active(0)
        employeeCombo.set_size_request(275,30)
        employeeBox.pack_default(employeeCombo)
        

        # RESIGNATION TYPE BOX
        resignationTypeBox = Box(Gtk.Orientation.HORIZONTAL)
        resignationTypeBox.set_margin_bottom(5)
        resignationTypeBox.set_margin_top(5)

        resignationTypeLabel = Gtk.Label()
        resignationTypeLabel.set_markup("Tipo de causa*")
        resignationTypeBox.pack_default(resignationTypeLabel)
        
        resignationTypeCombo = Gtk.ComboBoxText()
        resignationTypeCombo.set_entry_text_column(0)
        self.fillResignationTypeCombo(resignationTypeCombo)
        resignationTypeCombo.set_active(0)
        resignationTypeCombo.set_size_request(285,30)
        resignationTypeBox.pack_default(resignationTypeCombo)


        # MEMO BOX
        memoBox = Box(Gtk.Orientation.HORIZONTAL)
        memoBox.set_margin_top(5)
        memoBox.set_margin_bottom(5)
       
        memoLabel = Gtk.Label()
        memoLabel.set_text("Observação")
        
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

        confirmButton = Gtk.Button(label="Demitir")
        confirmButton.set_margin_left(15)
        confirmButton.set_size_request(100,30)
        confirmButton.connect("clicked", self.onConfirm)
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

    def onConfirm(self, button: Gtk.Button) -> None:
        self.__selectedEmployeeId = self.getEmployeeIdFromCombo()
        self.__selectedResignationTypeId = self.getResignationTypeFromCombo()
        self.__memo = self.getMemo(self.__memoInput)

        registration = self.__component.requestRegistration(
            self.__selectedEmployeeId,
            self.__selectedResignationTypeId,
            self.__memo
        )
        if registration:
            self.__component.changeEmployeeRegisterStatus(
                self.__selectedEmployeeId
            )
        self.refreshEmployeeCombo(self.__employeeCombo)
        self.refreshResignationTypeCombo(self.__resignationTypeCombo)
        self.refreshMemoInput(self.__memoInput)
        return

    def getData(self):
        self.__resignationTypes = self.__component.getResignationTypes()
        self.__employees = self.__component.getEmployees()
        return

    def getEmployeeIdFromCombo(self) -> int:
        try:
            id = self.__employeeCombo.get_active_text()
            id = int(re.findall(r'\d+',f"{id}")[0])
            return id 
        except IndexError:
            return 0

    def getResignationTypeFromCombo(self) -> str:
        try:
            res_type = self.__resignationTypeCombo.get_active_text()
            res_type = re.findall(r'\d+',f"{res_type}")[0]
            return res_type
        except IndexError:
            return 0

    def getMemo(self, memoInput: Gtk.Entry) -> str:
        return memoInput.get_text()

    def refreshEmployeeCombo(self, employeeCombo: Gtk.ComboBoxText) -> None:
        employeeCombo.remove_all()
        self.getData()
        self.fillEmployeeCombo(employeeCombo)
        return

    def refreshResignationTypeCombo(self, resignationTypeCombo: Gtk.ComboBoxText) -> None:
        resignationTypeCombo.remove_all()
        self.getData()
        self.fillResignationTypeCombo(resignationTypeCombo) 
        return

    def refreshMemoInput(self, memoInput: Gtk.Entry) -> None:
        memoInput.set_text("")
        return

    def fillEmployeeCombo(self, employeeCombo: Gtk.ComboBoxText) -> None:
        employeeCombo.append_text("0 - Escolha um funcionário")
        for employee in self.__employees:
            employeeCombo.append_text(
                f"{employee.id}" + " - " + f"{employee.legal_name[0:28]}")
        return

    def fillResignationTypeCombo(self, resignationTypeCombo: Gtk.ComboBoxText) -> None:
        resignationTypeCombo.append_text("0 - Selecione o tipo de causa")
        for resignationType in self.__resignationTypes:
            resignationTypeCombo.append_text(
                f"{resignationType.id}"+" - "+f"{resignationType.description}")
        return

    