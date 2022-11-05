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
        

    def get(self) -> Gtk.Box:
            mainBox = Box(orientation=Gtk.Orientation.VERTICAL)
            label = Gtk.Label()
            label.set_margin_bottom(30)
            mainBox.pack_start(label, False, False, 0)

            #Logica
            #cria LIST BOX
            #Preenche a listBOX com os objs de agendamento
            #Poe a comboBOX embaixo
            #Poe o botao em baixo
            #VOCE TEM 4 DIAS!!!!!!!!!!!!!!

            listBox = Gtk.ListBox()
            listBox.set_selection_mode(Gtk.SelectionMode.NONE)
            #self.add(listBox)
            
            '''
            row_1 = Gtk.ListBoxRow()
            box_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
            row_1.add(box_1)
            label_1 = Gtk.Label("TESTE TESTE")
            box_1.pack_start(label_1, True, True, 0)
            row_1.set_margin_top(5)
            row_1.set_margin_right(5)
            row_1.set_margin_bottom(5)
            row_1.set_margin_left(5)
            listBox.add(row_1)
            #Testando um segundo item
            row_2 = Gtk.ListBoxRow()
            box_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
            row_2.add(box_2)
            label_2 = Gtk.Label("TESTE TESTE 2!!!!!!!!!!!!")
            box_2.pack_start(label_2, True, True, 0)
            row_2.set_margin_top(5)
            row_2.set_margin_right(5)
            row_2.set_margin_bottom(5)
            row_2.set_margin_left(5)
            listBox.add(row_2)
            '''

            #agendamentos = self.__component.getAllScheduling()
            userID = self.__userContext.get().id
            userEmployee = self.__component.getEmployeeByUserID(userID)
            userEmployeeID = userEmployee.id
            agendamentos = self.__component.getSchedulingByEmployeeID(userEmployeeID)
            

            for agendamento in agendamentos:   
                if agendamento.job_state_id == 1:
                    row = Gtk.ListBoxRow()
                    box= Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
                    row.add(box)
                    jobName = self.__component.getJobById(agendamento.job_id).description
                    vehiclePlate = self.__component.getVehicleById(agendamento.vehicle_id).numberPlate
                    label = Gtk.Label(jobName + " " + str(agendamento.date) + " " + str(vehiclePlate))
                    box.pack_start(label, True, True, 0)
                    row.set_margin_top(5)
                    row.set_margin_right(5)
                    row.set_margin_bottom(5)
                    row.set_margin_left(5)
                    listBox.add(row)

            #fazendo comboboxteste
            #justificativasTeste = ["Euro", "US Dollars","British Pound","Japanese Yen", "Russian Ruble", "Mexican peso", "Swiss franc",]
            justificativasTeste = self.__component.getAllSchedulingStates()

            #lista_teste = self.__component.getAllSchedulingStates()
            #for i in lista_teste:
             #   print(i.description)
              #  justificativasTeste.append(i)


            combo_justificativas = Gtk.ComboBoxText()
            combo_justificativas.set_entry_text_column(0)
            #currency_combo.connect("changed", self.on_currency_combo_changed)
            for justificativa in justificativasTeste:
                combo_justificativas.append_text(justificativa.description)
                


            comboBoxLabel = Gtk.Label()
            comboBoxLabel.set_markup(toBig("Situação: "))

            botao_finalizar = Gtk.Button(label="Finalizar Serviço")


            mainBox.pack_start(listBox, False, False, 0)
            mainBox.pack_start(comboBoxLabel, False, False, 0)
            mainBox.pack_start(combo_justificativas, False, False, 0)
            mainBox.pack_start(botao_finalizar, False, False, 0)
            return mainBox

#Situaçao atual: Interface feia, mas pronta, porem os botoes nao fazem nada e nao mostro dados do banco, apenas dados teste
