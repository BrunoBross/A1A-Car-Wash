from package.app.client.modules.registeremployee.RegisterEmployeeComponent import (
    RegisterEmployeeComponent,
)
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk
from package.app.client.utils.markup import toBig
from package.app.client.gui.box.Box import Box


class RegisterEmployeeView(metaclass=Singleton):
    def __init__(self):
        self.__component = RegisterEmployeeComponent()
        self.__usernameFieldInput: Gtk.Widget
        self.__fullnameFieldInput: Gtk.Widget
        self.__passwordFieldInput: Gtk.Widget
        self.__salaryFieldInput: Gtk.Widget
        self.__jobLimitFieldInput: Gtk.Widget

        self.__usernameFieldEditInput: Gtk.Widget
        self.__fullnameFieldEditInput: Gtk.Widget
        self.__passwordFieldEditInput: Gtk.Widget
        self.__salaryFieldEditInput: Gtk.Widget
        self.__jobLimitFieldEditInput: Gtk.Widget

        self.__listStore = None
        self.__employeeCombo = None
        self.__employeeList = self.__component.getEmployeeList()
        self.__listBoxInput = None
        self.__employees = self.__component.getEmployees()

        self.__selectedEmployee = None

    def get(self) -> Gtk.Box:
        mainBox = Box(orientation=Gtk.Orientation.VERTICAL)

        # STACK GERAL
        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(500)
        # FIM STACK GERAL

        # INICIO DA LISTAGEM
        list_label = Gtk.Label()
        list_label.set_markup(toBig("Visualizar Funcionários"))
        list_label.set_margin_bottom(30)

        grid_list = Gtk.Grid(column_homogeneous=True, row_spacing=45)
        self.__listStore = Gtk.ListStore(int, str, str)
        for item in self.__employeeList:
            self.__listStore.append(list(item))
        treeView = Gtk.TreeView(model=self.__listStore)
        for i, title in enumerate(["ID", "Usuário", "Nome Completo"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(title, renderer, text=i)
            treeView.append_column(column)
        scrollableTreeList = Gtk.ScrolledWindow()
        scrollableTreeList.set_vexpand(True)
        grid_list.attach(scrollableTreeList, 0, 0, 400, 10)
        scrollableTreeList.add(treeView)

        self.__listBoxInput = scrollableTreeList

        listar = Box(orientation=Gtk.Orientation.VERTICAL)
        listar.pack_start(list_label, False, False, 0)
        listar.pack_start(grid_list, False, False, 0)
        # FINAL DA LISTAGEM

        # INICO DO CADASTRO
        register_label = Gtk.Label()
        register_label.set_markup(toBig("Cadastrar Funcionário"))
        register_label.set_margin_bottom(30)

        cadastroForm = self.getForm(isEdit=False)
        cadastrar = Box(orientation=Gtk.Orientation.VERTICAL)
        cadastrar.pack_start(register_label, False, False, 0)
        cadastrar.pack_start(cadastroForm, False, False, 0)
        # FINAL DO CADASTRO

        # INICIO EDICAO
        edit_label = Gtk.Label()
        edit_label.set_markup(toBig("Editar Funcionário"))
        edit_label.set_margin_bottom(30)

        employeeBox = Box(Gtk.Orientation.HORIZONTAL)
        employeeBox.set_margin_bottom(5)
        employeeBox.set_margin_top(5)

        employeeLabel = Gtk.Label()
        employeeLabel.set_markup("Funcionário")
        employeeBox.pack_default(employeeLabel)

        self.__employeeCombo = Gtk.ComboBoxText()
        self.__employeeCombo.set_entry_text_column(0)
        self.__employees = self.__component.getEmployees()
        if len(self.__component.getEmployees()) == 0:
            self.__employeeCombo.append_text("Nenhum funcionário cadastrado")
        else:
            self.__employeeCombo.append_text("Selecione um funcionário")
            for employee in self.__component.getEmployees():
                self.__employeeCombo.append_text(f"{employee.user.id} - {employee.user.username}")

        self.__employeeCombo.set_active(0)
        self.__employeeCombo.set_size_request(275, 30)
        self.__employeeCombo.connect("changed", self.changeComboBoxInput)
        employeeBox.pack_default(self.__employeeCombo)

        edicaoForm = self.getForm(isEdit=True)
        editar = Box(orientation=Gtk.Orientation.VERTICAL)
        editar.pack_start(edit_label, False, False, 0)
        editar.pack_start(employeeBox, False, False, 0)
        editar.pack_start(edicaoForm, False, False, 0)
        # FINAL EDICAO

        stack.add_titled(listar, "visualizar", "Visualizar")
        stack.add_titled(cadastrar, "cadastrar", "Cadastrar")
        stack.add_titled(editar, "editar", "Editar")
        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        mainBox.pack_start(stack_switcher, False, False, 0)
        mainBox.pack_start(stack, False, False, 0)

        return mainBox

    def changeComboBoxInput(self, _: Gtk.ComboBoxText):
        try:
            self.__selectedEmployee = int(_.get_active_text()[0])
        except ValueError:
            return

    def __registerEmployee(self, _: Gtk.Widget):
        self.__component.getState().addReference("username", self.__usernameFieldInput)
        self.__component.getState().addReference("fullname", self.__fullnameFieldInput)
        self.__component.getState().addReference("password", self.__passwordFieldInput)
        self.__component.getState().addReference("salary", self.__salaryFieldInput)
        self.__component.getState().addReference("limit", self.__jobLimitFieldInput)

        try:
            self.__component.requestRegisterEmployee()
        finally:
            self.updateList()
            self.updateEmployeeCombo()

    def __editEmployee(self, _: Gtk.Widget):
        self.__component.getState().addReference("usernameEdit", self.__usernameFieldEditInput)
        self.__component.getState().addReference("fullnameEdit", self.__fullnameFieldEditInput)
        self.__component.getState().addReference("passwordEdit", self.__passwordFieldEditInput)
        self.__component.getState().addReference("salaryEdit", self.__salaryFieldEditInput)
        self.__component.getState().addReference("limitEdit", self.__jobLimitFieldEditInput)

        try:
            self.__component.requestEditEmployee(self.__selectedEmployee)
        finally:
            self.updateList()
            self.updateEmployeeCombo()

    def updateList(self):
        self.__listStore.clear()
        self.__employeeList = self.__component.getEmployeeList()
        for item in self.__employeeList:
            self.__listStore.append(list(item))

    def updateEmployeeCombo(self):
        self.__employees = self.__component.getEmployees()
        self.get()

    def getForm(self, isEdit: bool):
        usernameFieldBox = Box(Gtk.Orientation.HORIZONTAL)
        usernameFieldLabel = Gtk.Label()
        usernameFieldInput = Gtk.Entry()
        if isEdit:
            usernameFieldLabel.set_text("Novo Nome de Usuario")
        else:
            usernameFieldLabel.set_text("Nome de Usuário *")
        usernameFieldInput.set_margin_top(5)
        usernameFieldInput.set_margin_right(5)
        usernameFieldInput.set_margin_bottom(5)
        usernameFieldInput.set_margin_left(5)
        usernameFieldBox.pack_default(usernameFieldLabel)
        usernameFieldBox.pack_default(usernameFieldInput)

        fullnameFieldBox = Box(Gtk.Orientation.HORIZONTAL)
        fullnameFieldLabel = Gtk.Label()
        fullnameFieldInput = Gtk.Entry()
        if isEdit:
            fullnameFieldLabel.set_text("Novo Nome Completo")
        else:
            fullnameFieldLabel.set_text("Nome Completo *")
        fullnameFieldInput.set_margin_top(5)
        fullnameFieldInput.set_margin_right(5)
        fullnameFieldInput.set_margin_bottom(5)
        fullnameFieldInput.set_margin_left(5)
        fullnameFieldBox.pack_default(fullnameFieldLabel)
        fullnameFieldBox.pack_default(fullnameFieldInput)

        passwordFieldBox = Box(Gtk.Orientation.HORIZONTAL)
        passwordFieldLabel = Gtk.Label()
        passwordFieldInput = Gtk.Entry()
        passwordFieldInput.set_visibility(False)
        if isEdit:
            passwordFieldLabel.set_text("Nova Senha Funcionário")
        else:
            passwordFieldLabel.set_text("Senha Funcionário *")
        passwordFieldInput.set_margin_top(5)
        passwordFieldInput.set_margin_right(5)
        passwordFieldInput.set_margin_bottom(5)
        passwordFieldInput.set_margin_left(5)
        passwordFieldBox.pack_default(passwordFieldLabel)
        passwordFieldBox.pack_default(passwordFieldInput)

        salaryFieldBox = Box(Gtk.Orientation.HORIZONTAL)
        salaryFieldLabel = Gtk.Label()
        salaryFieldInput = Gtk.Entry()
        if isEdit:
            salaryFieldLabel.set_text("Novo Salário Funcionário")
        else:
            salaryFieldLabel.set_text("Salário Funcionário *")
        salaryFieldInput.set_margin_top(5)
        salaryFieldInput.set_margin_right(5)
        salaryFieldInput.set_margin_bottom(5)
        salaryFieldInput.set_margin_left(5)
        salaryFieldBox.pack_default(salaryFieldLabel)
        salaryFieldBox.pack_default(salaryFieldInput)

        jobLimitFieldBox = Box(Gtk.Orientation.HORIZONTAL)
        jobLimitFieldLabel = Gtk.Label()
        jobLimitFieldInput = Gtk.Entry()
        if isEdit:
            jobLimitFieldLabel.set_text("Novo Limite de Serviços")
        else:
            jobLimitFieldLabel.set_text("Limite de Serviços *")
        jobLimitFieldInput.set_margin_top(5)
        jobLimitFieldInput.set_margin_right(5)
        jobLimitFieldInput.set_margin_bottom(5)
        jobLimitFieldInput.set_margin_left(5)
        jobLimitFieldBox.pack_default(jobLimitFieldLabel)
        jobLimitFieldBox.pack_default(jobLimitFieldInput)

        if isEdit:
            confirmButton = Gtk.Button(label="Editar")
            confirmButton.connect("clicked", self.__editEmployee)
            self.__usernameFieldEditInput = usernameFieldInput
            self.__fullnameFieldEditInput = fullnameFieldInput
            self.__passwordFieldEditInput = passwordFieldInput
            self.__salaryFieldEditInput = salaryFieldInput
            self.__jobLimitFieldEditInput = jobLimitFieldInput
        else:
            confirmButton = Gtk.Button(label="Cadastrar")
            confirmButton.connect("clicked", self.__registerEmployee)
            self.__usernameFieldInput = usernameFieldInput
            self.__fullnameFieldInput = fullnameFieldInput
            self.__passwordFieldInput = passwordFieldInput
            self.__salaryFieldInput = salaryFieldInput
            self.__jobLimitFieldInput = jobLimitFieldInput
        confirmButton.set_margin_top(30)

        form = Box(orientation=Gtk.Orientation.VERTICAL)
        form.pack_start(usernameFieldBox, False, False, 0)
        form.pack_start(fullnameFieldBox, False, False, 0)
        form.pack_start(passwordFieldBox, False, False, 0)
        form.pack_start(salaryFieldBox, False, False, 0)
        form.pack_start(jobLimitFieldBox, False, False, 0)
        form.pack_start(confirmButton, False, False, 0)

        return form
