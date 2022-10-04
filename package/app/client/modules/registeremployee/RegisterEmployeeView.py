from package.app.client.modules.registeremployee.RegisterEmployeeComponent import RegisterEmployeeComponent
from package.app.meta.Singleton import Singleton
from package.app.client.state.ComponentState import ComponentState
from package.app.client.gui.imports import Gtk
from package.app.client.utils.markup import toBig
from package.app.client.gui.box.Box import Box


class RegisterEmployeeView(metaclass=Singleton):
    def __init__(self):
        self.__component = RegisterEmployeeComponent()
        self.__state = ComponentState()

    def get(self) -> Gtk.Box:
        mainBox = Box(orientation=Gtk.Orientation.VERTICAL)
        label = Gtk.Label()
        label.set_markup(toBig("Cadastrar Funcionários"))
        label.set_margin_bottom(30)
        mainBox.pack_start(label, False, False, 0)

        usernameFieldBox = Box(Gtk.Orientation.HORIZONTAL)
        usernameFieldLabel = Gtk.Label()
        usernameFieldInput = Gtk.Entry()
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
        passwordFieldLabel.set_text("Senha *")
        passwordFieldInput.set_margin_top(5)
        passwordFieldInput.set_margin_right(5)
        passwordFieldInput.set_margin_bottom(5)
        passwordFieldInput.set_margin_left(5)
        passwordFieldBox.pack_default(passwordFieldLabel)
        passwordFieldBox.pack_default(passwordFieldInput)

        salaryFieldBox = Box(Gtk.Orientation.HORIZONTAL)
        salaryFieldLabel = Gtk.Label()
        salaryFieldInput = Gtk.Entry()
        salaryFieldLabel.set_text("Salário *")
        salaryFieldInput.set_margin_top(5)
        salaryFieldInput.set_margin_right(5)
        salaryFieldInput.set_margin_bottom(5)
        salaryFieldInput.set_margin_left(5)
        salaryFieldBox.pack_default(salaryFieldLabel)
        salaryFieldBox.pack_default(salaryFieldInput)

        confirmButton = Gtk.Button(label="Cadastrar")
        confirmButton.set_margin_top(30)
        confirmButton.connect("clicked", self.__onConfirm)

        self.__state.addReference("username", usernameFieldInput)
        self.__state.addReference("fullname", fullnameFieldInput)
        self.__state.addReference("password", passwordFieldInput)
        self.__state.addReference("salary", salaryFieldInput)

        mainBox.pack_start(usernameFieldBox, False, False, 0)
        mainBox.pack_start(fullnameFieldBox, False, False, 0)
        mainBox.pack_start(passwordFieldBox, False, False, 0)
        mainBox.pack_start(salaryFieldBox, False, False, 0)
        mainBox.pack_start(confirmButton, False, False, 0)

        return mainBox

    def __onConfirm(self, _: Gtk.Widget):
        self.__component.registerEmployee(
            Gtk.EntryBuffer.get_text(
                Gtk.Entry.get_buffer(self.__state.getReferenceById("username"))
            ),
            Gtk.EntryBuffer.get_text(
                Gtk.Entry.get_buffer(self.__state.getReferenceById("fullname"))
            ),
            Gtk.EntryBuffer.get_text(
                Gtk.Entry.get_buffer(self.__state.getReferenceById("password"))
            ),
            Gtk.EntryBuffer.get_text(
                Gtk.Entry.get_buffer(self.__state.getReferenceById("salary"))
            ),
        )
