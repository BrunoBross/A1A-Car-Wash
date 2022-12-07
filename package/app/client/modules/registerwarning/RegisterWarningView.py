from datetime import date, datetime
from package.app.client.event.EventEnum import EventEnum
from package.app.client.gui.box.Box import Box
from package.app.client.modules.registerwarning.RegisterWarningComponent import (
    RegisterWarningComponent,
)
from package.app.client.utils.markup import toBig
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk


class RegisterWarningView(metaclass=Singleton):
    def __init__(self):
        self.__component = RegisterWarningComponent()
        self.__warningList = self.__component.fetchInfo().existingWarnings
        self.__descriptionFieldInput: Gtk.Widget
        self.__listBoxInput = None
        self.__descriptionFieldEditInput: Gtk.Widget
        self.__listStore: Gtk.ListStore

    def get(self) -> Gtk.Box:
        mainBox = Box(orientation=Gtk.Orientation.VERTICAL)
        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(500)
        # FIM STACK GERAL

        # INICIO DA LISTAGEM
        list_label = Gtk.Label()
        list_label.set_markup(toBig("Visualizar Avisos"))
        list_label.set_margin_bottom(30)
        grid_list = Gtk.Grid(column_homogeneous=True, row_spacing=45)

        self.__listStore = Gtk.ListStore(int, str, str)
        for item in self.__warningList:
            self.__listStore.append(
                [item.id, item.description, datetime.strftime(item.date, "%Y-%m-%d")]
            )

        treeView = Gtk.TreeView(model=self.__listStore)
        for i, title in enumerate(["ID", "Descrição", "Data"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(title, renderer, text=i)
            treeView.append_column(column)

        scrollableTreeList = Gtk.ScrolledWindow()
        scrollableTreeList.set_vexpand(True)
        grid_list.attach(scrollableTreeList, 0, 0, 400, 10)
        scrollableTreeList.add(treeView)
        tree_selection = treeView.get_selection()
        tree_selection.connect("changed", self.__changeListBoxInput)

        delete_button = Gtk.Button(label="Deletar Aviso")
        delete_button.connect("clicked", self.__deleteWarning)
        delete_button.set_margin_top(30)

        listar = Box(orientation=Gtk.Orientation.VERTICAL)
        listar.pack_start(list_label, False, False, 0)
        listar.pack_start(grid_list, False, False, 0)
        listar.pack_start(delete_button, False, False, 0)
        # FINAL DA LISTAGEM

        # INICO DO CADASTRO
        register_label = Gtk.Label()
        register_label.set_markup(toBig("Cadastrar Aviso"))
        register_label.set_margin_bottom(30)

        cadastroForm = self.__getForm()
        cadastrar = Box(orientation=Gtk.Orientation.VERTICAL)
        cadastrar.pack_start(register_label, False, False, 0)
        cadastrar.pack_start(cadastroForm, False, False, 0)
        # FINAL DO CADASTRO

        # INICIO EDICAO
        edit_label = Gtk.Label()
        edit_label.set_markup(toBig("Editar Aviso"))
        edit_label.set_margin_bottom(30)

        edicaoForm = self.__getForm(isEdit=True)
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

    def __changeListBoxInput(self, _):
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

    def __setInputData(self) -> None:
        self.__warningList = self.__component.fetchInfo().existingWarnings
        self.__listStore.clear()
        for item in self.__warningList:
            self.__listStore.append(
                [item.id, item.description, datetime.strftime(item.date, "%Y-%m-%d")]
            )

    def __reset(self, _):
        self.__setInputData()

    def updateList(self):
        self.__listStore.clear()
        self.__warningList = self.__component.fetchInfo().existingWarnings
        for item in self.__warningList:
            self.__listStore.append(
                [item.id, item.description, datetime.strftime(item.date, "%Y-%m-%d")]
            )

    def __getForm(self, isEdit: bool = False) -> Box:
        descriptionFieldBox = Box(Gtk.Orientation.HORIZONTAL)
        descriptionFieldLabel = Gtk.Label()
        descriptionFieldInput = Gtk.Entry()

        if isEdit:
            descriptionFieldLabel.set_text("Nova descrição do aviso")
        else:
            descriptionFieldLabel.set_text("Descrição do aviso *")
        descriptionFieldInput.set_margin_top(5)
        descriptionFieldInput.set_margin_right(5)
        descriptionFieldInput.set_margin_bottom(5)
        descriptionFieldInput.set_margin_left(5)
        descriptionFieldBox.pack_default(descriptionFieldLabel)
        descriptionFieldBox.pack_default(descriptionFieldInput)

        if isEdit:
            confirmButton = Gtk.Button(label="Editar")
            confirmButton.connect("clicked", self.__editWarning)
            self.__descriptionFieldEditInput = descriptionFieldInput
        else:
            confirmButton = Gtk.Button(label="Cadastrar")
            confirmButton.connect("clicked", self.__registerWarning)
            self.__descriptionFieldInput = descriptionFieldInput
        confirmButton.set_margin_top(30)

        form = Box(orientation=Gtk.Orientation.VERTICAL)
        form.pack_start(descriptionFieldBox, False, False, 0)
        form.pack_start(confirmButton, False, False, 0)

        return form

    def __registerWarning(self, _: Gtk.Widget):
        self.__component.getState().addReference(
            "description", self.__descriptionFieldInput
        )

        try:
            self.__component.requestRegisterWarning()
        finally:
            self.updateList()

    def __editWarning(self, _: Gtk.Widget):
        self.__component.getState().addReference(
            "descriptionEdit", self.__descriptionFieldEditInput
        )

        try:
            self.__component.requestEditWarning(self.__listBoxInput[0])
        finally:
            self.updateList()

    def __deleteWarning(self, _) -> None:
        try:
            self.__component.requestDeleteWarning(self.__listBoxInput[0])
        finally:
            self.updateList()
