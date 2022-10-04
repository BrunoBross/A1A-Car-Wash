from package.app.client.modules.employee.EmployeeComponent import EmployeeComponent
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk
from package.app.client.utils.markup import toBig
from package.app.client.gui.box.Box import Box
from package.app.client.state.UserContext import UserContext


class EmployeeView(metaclass=Singleton):
    def __init__(self):
        self.__userContext = UserContext()
        self.__component = EmployeeComponent()

    def get(self) -> Gtk.Box:
        mainBox = Box(orientation=Gtk.Orientation.VERTICAL)
        label = Gtk.Label()
        label.set_markup(toBig(f"Tela do Funcionário: {self.getEmployeeFullNameByUsername()}"))
        label.set_margin_bottom(30)
        mainBox.pack_start(label, False, False, 0)

        return mainBox

    # APENAS PARA TESTE E DIZER QUE ESTA LOGANDO COM O CARA CERTO
    def getEmployeeFullNameByUsername(self):
        username = self.__userContext.get().username
        return self.__component.getEmployeeFullNameByUsername(username)

