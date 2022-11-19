from package.app.client.gui.box.Box import Box
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk
from package.app.client.utils.markup import toBig
from package.app.client.modules.schedulingemployee.EmployeeSchedullingComponent import (
    EmployeeSchedulingComponent,
)
from package.app.client.state.UserContext import UserContext


class EmployeeSchedulingView(metaclass=Singleton):
    def __init__(self):
        self.__userContext = UserContext()
        self.__component = EmployeeSchedulingComponent()
        self.__schedulingList = self.__component.getSchedulingList()
        self.__warningList = self.__component.getWarningList()
        self.__justificativasDict = {}
        self.__comboJustificativasInput = None
        self.__listBoxInput = None
        self.__listBoxInput_warning = None
        self.__listStore = None
        self.__listStore_warning = None

    def get(self) -> Gtk.Box:
        mainBox = Box(orientation=Gtk.Orientation.VERTICAL)
        title = Gtk.Label()
        title.set_markup(toBig("Agendamentos"))
        title.set_margin_bottom(30)
        mainBox.pack_start(title, False, False, 0)

        # LIST BOX WARNING
        grid_warning = Gtk.Grid(column_homogeneous=True, row_spacing=45)
        self.__listStore_warning = Gtk.ListStore(str, bool)
        for item in self.__warningList:
            self.__listStore_warning.append(list(item))
        treeView_warning = Gtk.TreeView(model=self.__listStore_warning)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Quadro de avisos", renderer_text, text=0)
        treeView_warning.append_column(column_text)

        renderer_toggle = Gtk.CellRendererToggle()
        renderer_toggle.connect("toggled", self.on_cell_toggled)
        column_toggle = Gtk.TreeViewColumn("Lido", renderer_toggle, active=1)
        treeView_warning.append_column(column_toggle)

        scrollableTreeList_warning = Gtk.ScrolledWindow()
        scrollableTreeList_warning.set_vexpand(True)
        grid_warning.attach(scrollableTreeList_warning, 0, 0, 300, 10)
        scrollableTreeList_warning.add(treeView_warning)
        tree_selection_warning = treeView_warning.get_selection()
        tree_selection_warning.connect("changed", self.checkAsRead)

        # LIST BOX
        grid = Gtk.Grid(column_homogeneous=True, row_spacing=45)
        self.__listStore = Gtk.ListStore(str, str, str)
        for item in self.__schedulingList:
            self.__listStore.append(list(item))
        treeView = Gtk.TreeView(model=self.__listStore)
        for i, title in enumerate(["Placa do Carro", "Tipo de Limpeza", "Data"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(title, renderer, text=i)
            treeView.append_column(column)
        scrollableTreeList = Gtk.ScrolledWindow()
        scrollableTreeList.set_vexpand(True)
        grid.attach(scrollableTreeList, 0, 0, 300, 10)
        scrollableTreeList.add(treeView)
        tree_selection = treeView.get_selection()
        tree_selection.connect("changed", self.changeListBoxInput)

        # COMBO BOX
        comboJustificativasBox = Box(Gtk.Orientation.HORIZONTAL)
        comboJustificativas = Gtk.ComboBoxText()
        comboJustificativasLabel = Gtk.Label()
        comboJustificativasLabel.set_markup(toBig("Selecione um status:"))
        comboJustificativas.set_entry_text_column(0)
        justificativasList = self.__component.getAllSchedulingStates()
        for justificativa in justificativasList:
            if justificativa.id != 1:
                self.__justificativasDict[justificativa.description] = justificativa.id
                comboJustificativas.append_text(justificativa.description)
        comboJustificativasBox.pack_default(comboJustificativasLabel)
        comboJustificativasBox.pack_default(comboJustificativas)
        comboJustificativas.connect("changed", self.changeComboBoxInput)

        # BOTAO
        confirmButton = Gtk.Button(label="Finalizar serviço")
        confirmButton.set_margin_top(30)
        confirmButton.connect("clicked", self.onConfirm)

        # INPUTS
        self.__comboJustificativasInput = comboJustificativas
        self.__listBoxInput = scrollableTreeList
        self.__listBoxInput_warning = scrollableTreeList_warning
        self.__listStore_warning = scrollableTreeList_warning

        # ADICIONAR NA TELA
        divHorizontal = Box(orientation=Gtk.Orientation.HORIZONTAL)
        divHorizontal.pack_start(grid_warning, False, False, 10)
        divHorizontal.pack_start(grid, False, False, 0)

        mainBox.pack_start(divHorizontal, False, False, 0)
        mainBox.pack_start(comboJustificativasBox, False, False, 0)
        mainBox.pack_start(confirmButton, False, False, 0)

        return mainBox

    def changeComboBoxInput(self, _):
        self.__comboJustificativasInput = _.get_active_text()

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

    def onConfirm(self, _: Gtk.Widget):
        self.__component.updateJobStateID(
            self.__listBoxInput, self.__comboJustificativasInput
        )
        self.updateList()

    def updateList(self):
        self.__listStore.clear()
        self.__schedulingList = self.__component.getSchedulingList()
        for item in self.__schedulingList:
            self.__listStore.append(list(item))

    def checkAsRead(self, _):
        self.__listBoxInput_warning = _.get_selected_rows()

    def on_cell_toggled(self, widget, path):
        self.__listStore_warning[path][1] = not self.__listStore_warning[path][1]

