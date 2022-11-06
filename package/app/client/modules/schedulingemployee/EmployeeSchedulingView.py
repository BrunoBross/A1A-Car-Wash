from package.app.client.gui.box.Box import Box
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk
from package.app.client.utils.markup import toBig
from package.app.client.modules.schedulingemployee.EmployeeSchedullingComponent import EmployeeSchedulingComponent


from package.app.client.state.UserContext import UserContext

class EmployeeSchedulingView(metaclass=Singleton):
    def __init__(self):
        self.__userContext = UserContext()
        self.__component = EmployeeSchedulingComponent()
        self.__idAgendamento = None
        self.__idJustificativa = None
        self.__agendamentosDict = {}
        self.__justificativasDict = {}

    def get(self) -> Gtk.Box:
            mainBox = Box(orientation=Gtk.Orientation.VERTICAL)
            label = Gtk.Label()
            label.set_margin_bottom(30)
            mainBox.pack_start(label, False, False, 0)

            #LIST BOX
            grid = Gtk.Grid(column_homogeneous=True, row_spacing=20)

            listStore = Gtk.ListStore(str, str)
            for item in self.__component.getSchedulingList():
                listStore.append(list(item))

            treeView = Gtk.TreeView(model=listStore)
            for i, title in enumerate(["Placa do Carro", "Tipo de Limpeza"]):
                renderer = Gtk.CellRendererText()
                column = Gtk.TreeViewColumn(title, renderer, text=i)
                treeView.append_column(column)

            scrollableTreeList = Gtk.ScrolledWindow()
            scrollableTreeList.set_vexpand(True)
            grid.attach(scrollableTreeList, 0, 0, 4, 10)
            scrollableTreeList.add(treeView)

            #COMBO BOX
            comboJustificativasBox = Box(Gtk.Orientation.HORIZONTAL)
            comboJustificativas = Gtk.ComboBoxText()
            comboJustificativasLabel = Gtk.Label()
            comboJustificativasLabel.set_markup(toBig("Selecione um status:"))
            comboJustificativas.set_entry_text_column(0)
            justificativasList = self.__component.getAllSchedulingStates()
            for justificativa in justificativasList:
                self.__justificativasDict[justificativa.description] = justificativa.id
                comboJustificativas.append_text(justificativa.description)
            comboJustificativasBox.pack_default(comboJustificativasLabel)
            comboJustificativasBox.pack_default(comboJustificativas)

            #ADICIONAR NA TELA
            mainBox.pack_start(grid, False, False, 0)
            mainBox.pack_start(comboJustificativasBox, False, False, 0)
            return mainBox

    def onSchedulingComboChanged(self, combo):
        self.__idJustificativa = self.__justificativasDict[combo.get_active_text()]
        print(self.__idJustificativa)

    def onSchedulingListClicked(self, rowButton):
        print(rowButton.get_label())
        self.__idAgendamento = self.__agendamentosDict[rowButton.get_label()]
        print(self.__idAgendamento)
    
    def onFinalizadoClicked(self, button:Gtk.Widget):
        schedulingKeys = self.__idAgendamento
        newJobStateId = self.__idJustificativa
        self.__component.updateJobStateID(schedulingKeys, newJobStateId)
        print(button)
        print(self.__idAgendamento)
        print(self.__idJustificativa)
        #self.refreshWindow()
    
    
    #def removeListRow(self, listBox:Gtk.Widget, SchedulingKeys: str):
