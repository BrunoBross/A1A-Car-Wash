from package.app.client.gui.box.Box import Box
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk
from package.app.client.utils.markup import toBig
from package.app.client.modules.registervehicle.RegisterVehicleComponent import (
    RegisterVehicleComponent,
)


class RegisterVehicleView(metaclass=Singleton):
    def __init__(self):
        self.__component = RegisterVehicleComponent()
        self.__numberPlateInput: Gtk.Widget

        self.__listStore = None
        self.__vehicleCombo = None
        self.__vehicleList = self.__component.getVehicleList()
        self.__listBoxInput = None
        self.__selectedVehicle = None
        self.__vehicles = self.__component.getAllVehicles()
        self.__numberPlateFieldInput: Gtk.Widget
        self.__numberPlateFieldEditInput: Gtk.Widget
        
        

    def get(self) -> Gtk.Box:
        mainBox = Box(orientation=Gtk.Orientation.VERTICAL)

        # STACK GERAL
        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(500)
        # FIM STACK GERAL

        # INICIO DA LISTAGEM
        list_label = Gtk.Label()
        list_label.set_markup(toBig("Visualizar Veiculos"))
        list_label.set_margin_bottom(30)

        grid_list = Gtk.Grid(column_homogeneous=True, row_spacing=45)
        self.__listStore = Gtk.ListStore(int, str, str)
        for item in self.__vehicleList:
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
        #fim da listagem

        # INICO DO CADASTRO
        register_label = Gtk.Label()
        register_label.set_markup(toBig("Cadastrar Veiculo"))
        register_label.set_margin_bottom(30)

        cadastroForm = self.getForm(isEdit=False)
        cadastrar = Box(orientation=Gtk.Orientation.VERTICAL)
        cadastrar.pack_start(register_label, False, False, 0)
        cadastrar.pack_start(cadastroForm, False, False, 0)
        # FINAL DO CADASTRO

        # INICIO EDICAO
        edit_label = Gtk.Label()
        edit_label.set_markup(toBig("Editar Veiculo"))
        edit_label.set_margin_bottom(30)

        vehicleBox = Box(Gtk.Orientation.HORIZONTAL)
        vehicleBox.set_margin_bottom(5)
        vehicleBox.set_margin_top(5)

        vehicleLabel = Gtk.Label()
        vehicleLabel.set_markup("Veiculo")
        vehicleBox.pack_default(vehicleLabel)

        self.__vehicleCombo = Gtk.ComboBoxText()
        self.__vehicleCombo.set_entry_text_column(0)
        self.__vehicles = self.__component.getAllVehicles()
        if len(self.__component.getAllVehicles()) == 0:
            self.__vehicleCombo.append_text("Nenhum veiculo cadastrado")
        else:
            self.__vehicleCombo.append_text("Selecione um veiculo")
            for vehicle in self.__component.getAllVehicles():
                self.__vehicleCombo.append_text(f"{vehicle.id} - {vehicle.numberPlate}")

        self.__vehicleCombo.set_active(0)
        self.__vehicleCombo.set_size_request(275, 30)
        self.__vehicleCombo.connect("changed", self.changeComboBoxInput)
        vehicleBox.pack_default(self.__vehicleCombo)

        edicaoForm = self.getForm(isEdit=True)
        editar = Box(orientation=Gtk.Orientation.VERTICAL)
        editar.pack_start(edit_label, False, False, 0)
        editar.pack_start(vehicleBox, False, False, 0)
        editar.pack_start(edicaoForm, False, False, 0)
        # FINAL EDICAO

        #stacks
        stack.add_titled(listar, "visualizar", "Visualizar")
        stack.add_titled(cadastrar, "cadastrar", "Cadastrar")
        stack.add_titled(editar, "editar", "Editar")
        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        mainBox.pack_start(stack_switcher, False, False, 0)
        mainBox.pack_start(stack, False, False, 0)

        return mainBox

    def __onConfirm(self, _: Gtk.Widget):
        self.__component.getState().addReference("numberPlate", self.__numberPlateFieldInput)
        self.__component.requestCreateVehicle()

    def __registerVehicle(self, _: Gtk.Widget):
        self.__component.getState().addReference("numberPlate", self.__numberPlateFieldInput)

        try:
            self.__component.requestCreateVehicle()
        finally:
            self.updateList()
            self.updateVehicleCombo()

    def __editVehicle(self, _: Gtk.Widget):
        self.__component.getState().addReference("numberPlateEdit", self.__numberPlateFieldInput)
        try:
            self.__component.requestEditEmployee(self.__selectedVehicle)
        finally:
            self.updateList()
            self.updateVehicleCombo()

    def changeComboBoxInput(self, _: Gtk.ComboBoxText):
        try:
            self.__selectedVehicle = int(_.get_active_text()[0])
        except ValueError:
            return

    def updateVehicleCombo(self):
        self.__vehicles = self.__component.getAllVehicles()
        self.get()

    def updateList(self):
        self.__listStore.clear()
        self.__vehicleList = self.__component.getVehicleList()
        for item in self.__vehicleList:
            self.__listStore.append(list(item))

    def getForm(self, isEdit:bool):
        numberPlateFieldBox = Box(Gtk.Orientation.HORIZONTAL)
        numberPlateFieldLabel = Gtk.Label()
        numberPlateFieldInput = Gtk.Entry()
        if isEdit:
            numberPlateFieldLabel.set_text("Nova placa do veiculo")
        else:
            numberPlateFieldLabel.set_text("Placa do veiculo *")
        numberPlateFieldInput.set_margin_top(5)
        numberPlateFieldInput.set_margin_right(5)
        numberPlateFieldInput.set_margin_bottom(5)
        numberPlateFieldInput.set_margin_left(5)
        numberPlateFieldBox.pack_default(numberPlateFieldLabel)
        numberPlateFieldBox.pack_default(numberPlateFieldInput)


        if isEdit:
            confirmButton = Gtk.Button(label="Editar")
            confirmButton.connect("clicked", self.__editVehicle)
            self.__numberPlateFieldEditInput = numberPlateFieldInput
            
        else:
            confirmButton = Gtk.Button(label="Cadastrar")
            confirmButton.connect("clicked", self.__registerVehicle)
            self.__numberPlateFieldInput = numberPlateFieldInput
        confirmButton.set_margin_top(30)

        form = Box(orientation=Gtk.Orientation.VERTICAL)
        form.pack_start(numberPlateFieldBox, False, False, 0)
        form.pack_start(confirmButton, False, False, 0)

        return form
