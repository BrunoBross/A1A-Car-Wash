from package.app.client.gui.box.Box import Box
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk
from package.app.client.utils.markup import toBig
from package.app.client.modules.employee.components.EmployeeSchedullingComponent import EmployeeSchedulingComponent


from package.app.client.state.UserContext import UserContext

class EmployeeSchedulingView(metaclass=Singleton):
    def __init__(self):
        self.__userContext = UserContext()
        self.__component = EmployeeSchedulingComponent()
        #self.__Schedulign_component = 
        self.__idAgendamento = None
        self.__idJustificativa = None
        self.__agendamentosDict = {}
        self.__justificativasDict = {}



    def get(self) -> Gtk.Box:
            mainBox = Box(orientation=Gtk.Orientation.VERTICAL)
            label = Gtk.Label()
            label.set_margin_bottom(30)
            mainBox.pack_start(label, False, False, 0)

            #Logica
            #cria LIST BOX OK
            #Preenche a listBOX com os objs de agendamento OK
            #Poe a comboBOX embaixo 
            #Poe o botao em baixo
            #VOCE TEM 4 DIAS!!!!!!!!!!!!!!

            listBox = Gtk.ListBox()
            listBox.set_selection_mode(Gtk.SelectionMode.NONE)
           

            #agendamentos = self.__component.getAllScheduling()
            userID = self.__userContext.get().id
            userEmployee = self.__component.getEmployeeByUserID(userID)
            userEmployeeID = userEmployee.id
            agendamentos = self.__component.getSchedulingByEmployeeID(userEmployeeID)
            
           

            for agendamento in agendamentos:   
                if agendamento.job_state_id == 1:
                    
                    jobName = self.__component.getJobById(agendamento.job_id).description
                    vehiclePlate = self.__component.getVehicleById(agendamento.vehicle_id).numberPlate
                    nomeAgendamento = jobName + " " + str(agendamento.date) + " " + str(vehiclePlate) 
                    idAgendamento = str(agendamento.employee_id) + " " + str(agendamento.job_id) +" " + str(agendamento.vehicle_id) +  " " + str(agendamento.date) 
                    
                    self.__agendamentosDict[nomeAgendamento] = idAgendamento

                    row = Gtk.ListBoxRow()
                    box= Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
                    row.add(box)
                    
                    buttonSelect = Gtk.Button(label=nomeAgendamento)
                    buttonSelect.connect("clicked", self.onSchedulingListClicked)
                    box.pack_start(buttonSelect, True, True, 0)

                    #label = Gtk.Label(nomeAgendamento)
                    #box.pack_start(label, True, True, 0)

                    #buttonSelect = Gtk.Button(label="Selecionar")
                    #buttonSelect.connect("clicked", self.onSchedulingListClicked)
                    #box.pack_start(buttonSelect, True, True, 0)
                    row.set_margin_top(5)
                    row.set_margin_right(5)
                    row.set_margin_bottom(5)
                    row.set_margin_left(5)

                    #row.connect("row_selected", self.onSchedulingListClicked)
                    listBox.add(row)

            comboBoxLabel = Gtk.Label()
            comboBoxLabel.set_markup(toBig("Situação: "))

            comboJustificativas = Gtk.ComboBoxText()
            comboJustificativas.set_entry_text_column(0)

            
            justificativasList = self.__component.getAllSchedulingStates()
            for justificativa in justificativasList:
                self.__justificativasDict[justificativa.description] = justificativa.id
                comboJustificativas.append_text(justificativa.description)

            comboJustificativas.connect("changed", self.onSchedulingComboChanged)

            botaoFinalizar = Gtk.Button(label="Finalizar Serviço")
            botaoFinalizar.connect("clicked", self.onFinalizadoClicked)

            mainBox.pack_start(listBox, False, False, 0)
            mainBox.pack_start(comboBoxLabel, False, False, 0)
            mainBox.pack_start(comboJustificativas, False, False, 0)
            mainBox.pack_start(botaoFinalizar, False, False, 0)
            return mainBox

    def onSchedulingComboChanged(self, combo):
        self.__idJustificativa = self.__justificativasDict[combo.get_active_text()]
        print(self.__idJustificativa)

    def onSchedulingListClicked(self, rowButton):
        print(rowButton.get_label())
        self.__idAgendamento = self.__agendamentosDict[rowButton.get_label()]
        print(self.__idAgendamento)
    
    def onFinalizadoClicked(self, button:Gtk.Widget):
        print(button)
        print(self.__idAgendamento)
        print(self.__idJustificativa)