from package.app.client.modules.registerjob.RegisterJobComponent import (
    RegisterJobComponent,
)
from package.app.meta.Singleton import Singleton
from package.app.client.utils.markup import toBig
from package.app.client.gui.box.Box import Box
from package.app.client.gui.imports import Gtk


class RegisterJobView(metaclass=Singleton):
    def __init__(self):
        self.__component = RegisterJobComponent()

        self.__jobNameInput: Gtk.Widget
        self.__jobValueInput: Gtk.Widget

        self.__jobNameEditInput: Gtk.Widget
        self.__jobValueEditInput: Gtk.Widget

        self.__listStore = None
        self.__jobList = self.__component.getJobList()
        self.__listBoxInput = None

    def get(self) -> Gtk.Box:
        mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # STACK GERAL
        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(500)
        # FIM STACK GERAL

        # INICIO DA LISTAGEM
        list_label = Gtk.Label()
        list_label.set_markup(toBig("Visualizar Serviços"))
        list_label.set_margin_bottom(30)

        grid_list = Gtk.Grid(column_homogeneous=True, row_spacing=45)
        self.__listStore = Gtk.ListStore(int, str, str)
        for item in self.__jobList:
            self.__listStore.append(list(item))
        treeView = Gtk.TreeView(model=self.__listStore)
        for i, title in enumerate(["ID", "Descrição", "Preço"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(title, renderer, text=i)
            treeView.append_column(column)
        scrollableTreeList = Gtk.ScrolledWindow()
        scrollableTreeList.set_vexpand(True)
        grid_list.attach(scrollableTreeList, 0, 0, 400, 10)
        scrollableTreeList.add(treeView)
        tree_selection = treeView.get_selection()
        tree_selection.connect("changed", self.changeListBoxInput)

        delete_button = Gtk.Button(label="Deletar Serviço")
        delete_button.connect("clicked", self.__deleteJob)
        delete_button.set_margin_top(30)

        listar = Box(orientation=Gtk.Orientation.VERTICAL)
        listar.pack_start(list_label, False, False, 0)
        listar.pack_start(grid_list, False, False, 0)
        listar.pack_start(delete_button, False, False, 0)
        # FINAL DA LISTAGEM

        # INICO DO CADASTRO
        register_label = Gtk.Label()
        register_label.set_markup(toBig("Cadastrar Serviço"))
        register_label.set_margin_bottom(30)

        cadastroForm = self.getForm(isEdit=False)
        cadastrar = Box(orientation=Gtk.Orientation.VERTICAL)
        cadastrar.pack_start(register_label, False, False, 0)
        cadastrar.pack_start(cadastroForm, False, False, 0)
        # FINAL DO CADASTRO

        # INICIO EDICAO
        edit_label = Gtk.Label()
        edit_label.set_markup(toBig("Editar Serviço"))
        edit_label.set_margin_bottom(30)

        edicaoForm = self.getForm(isEdit=True)
        editar = Box(orientation=Gtk.Orientation.VERTICAL)
        editar.pack_start(edit_label, False, False, 0)
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

    def __registerJob(self, _: Gtk.Widget):
        self.__component.getState().addReference("jobName", self.__jobNameInput)
        self.__component.getState().addReference("jobValue", self.__jobValueInput)

        try:
            self.__component.requestRegister()
        finally:
            self.updateList()

    def __editJob(self, _: Gtk.Widget):
        self.__component.getState().addReference("jobName", self.__jobNameEditInput)
        self.__component.getState().addReference("jobValue", self.__jobValueEditInput)

        try:
            self.__component.requestEdit(self.__listBoxInput)
        finally:
            self.updateList()

    def __deleteJob(self, _: Gtk.Button):
        try:
            self.__component.requestDelete(self.__listBoxInput)
        finally:
            self.updateList()

    def getForm(self, isEdit: bool):
        jobNameBox = Box(Gtk.Orientation.HORIZONTAL)
        jobNameLabel = Gtk.Label()
        jobNameInput = Gtk.Entry()
        if isEdit:
            jobNameLabel.set_text("Novo Nome do Serviço")
        else:
            jobNameLabel.set_text("Nome do Serviço *")
        jobNameInput.set_margin_top(5)
        jobNameInput.set_margin_right(5)
        jobNameInput.set_margin_bottom(5)
        jobNameInput.set_margin_left(5)
        jobNameBox.pack_default(jobNameLabel)
        jobNameBox.pack_default(jobNameInput)

        jobValueBox = Box(Gtk.Orientation.HORIZONTAL)
        jobValueLabel = Gtk.Label()
        jobValueInput = Gtk.Entry()
        if isEdit:
            jobValueLabel.set_text("Novo Valor do Serviço")
        else:
            jobValueLabel.set_text("Preço do Serviço *")
        jobValueInput.set_margin_top(5)
        jobValueInput.set_margin_right(5)
        jobValueInput.set_margin_bottom(5)
        jobValueInput.set_margin_left(5)
        jobValueBox.pack_default(jobValueLabel)
        jobValueBox.pack_default(jobValueInput)

        if isEdit:
            confirmButton = Gtk.Button(label="Editar")
            confirmButton.connect("clicked", self.__editJob)
            self.__jobNameEditInput = jobNameInput
            self.__jobValueEditInput = jobValueInput
        else:
            confirmButton = Gtk.Button(label="Cadastrar")
            confirmButton.connect("clicked", self.__registerJob)
            self.__jobNameInput = jobNameInput
            self.__jobValueInput = jobValueInput
        confirmButton.set_margin_top(30)

        form = Box(orientation=Gtk.Orientation.VERTICAL)
        form.pack_start(jobNameBox, False, False, 0)
        form.pack_start(jobValueBox, False, False, 0)
        form.pack_start(confirmButton, False, False, 0)

        return form

    def changeListBoxInput(self, _):
        self.__listBoxInput = _.get_selected_rows()
        (model, pathlist) = _.get_selected_rows()
        for path in pathlist:
            tree_iter = model.get_iter(path)
            value = [
                model.get_value(tree_iter, 0),
                model.get_value(tree_iter, 1),
                model.get_value(tree_iter, 2),
            ]
            self.__listBoxInput = value

    def updateList(self):
        self.__listStore.clear()
        self.__jobList = self.__component.getJobList()
        for item in self.__jobList:
            self.__listStore.append(list(item))
