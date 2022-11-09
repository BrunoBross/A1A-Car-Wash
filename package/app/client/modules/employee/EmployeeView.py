from package.app.client.modules.employee.EmployeeComponent import EmployeeComponent
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk
from package.app.client.utils.markup import toBig
from package.app.client.gui.box.Box import Box


class EmployeeView(metaclass=Singleton):
    def __init__(self):
        self.__component = EmployeeComponent()

    def get(self) -> Gtk.Box:
        mainBox = Box(orientation=Gtk.Orientation.VERTICAL)
        label = Gtk.Label()
        label.set_markup(toBig(f"Tela do Funcionário: {self.__getEmployeeFullName()}"))
        label.set_margin_bottom(30)
        mainBox.pack_start(label, False, False, 0)

        return mainBox

    def __getEmployeeFullName(self) -> str:
        user_id = self.component.getUserContext().get().id
        return self.__component.getEmployeeByUserId(user_id).legalName
