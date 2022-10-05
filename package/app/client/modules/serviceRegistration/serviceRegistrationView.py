from ast import Gt
from package.app.client.modules.serviceRegistration.serviceRegistrationComponent import ServiceRegistrationComponent
from package.app.meta.Singleton import Singleton
from package.app.client.state.ComponentState import ComponentState
from package.app.client.utils.markup import toBig
from package.app.client.gui.box.Box import Box
from package.app.client.gui.imports import Gtk
from package.app.template.IAppComponent import IAppComponent


class ServiceRegistrationView(metaclass=Singleton):
    def __init__(self):
        self.__component = ServiceRegistrationComponent()
        self.__state = ComponentState() 

    def get(self) -> Gtk.Box:

        mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        label = Gtk.Label()
        label.set_markup(toBig("Cadastrar Serviço"))
        label.set_margin_bottom(30)
        mainBox.pack_start(label, False, False, 0)

        serviceNameBox = Box(Gtk.Orientation.HORIZONTAL)
        serviceNameFieldLabel = Gtk.Label()
        serviceNameFieldLabel.set_text("Nome do serviço")
        serviceNameFieldLabel.set_margin_top(5)
        serviceNameFieldLabel.set_margin_left(5)
        serviceNameFieldLabel.set_margin_bottom(5)
        serviceNameFieldLabel.set_margin_right(5)
        serviceNameBox.pack_default(serviceNameFieldLabel)
        serviceNameFieldInput = Gtk.Entry()
        serviceNameFieldInput.set_margin_top(5)
        serviceNameFieldInput.set_margin_left(5)
        serviceNameFieldInput.set_margin_bottom(5)
        serviceNameFieldInput.set_margin_right(5)
        serviceNameBox.pack_default(serviceNameFieldInput)

        priceBox = Box(Gtk.Orientation.HORIZONTAL)
        priceFieldLabel = Gtk.Label()
        priceFieldLabel.set_text("Preço do serviço")
        priceFieldLabel.set_margin_top(5)
        priceFieldLabel.set_margin_left(5)
        priceFieldLabel.set_margin_bottom(5)
        priceFieldLabel.set_margin_right(5)
        priceBox.pack_default(priceFieldLabel)
        priceFieldInput = Gtk.Entry()
        priceFieldInput.set_margin_top(5)
        priceFieldInput.set_margin_left(5)
        priceFieldInput.set_margin_bottom(5)
        priceFieldInput.set_margin_right(5)
        priceBox.pack_default(priceFieldInput)    

        confirmButton = Gtk.Button(label="Cadastrar")
        confirmButton.set_margin_top(30)
        confirmButton.connect("clicked", self.__onConfirm)

        self.__state.addReference("service_name", serviceNameFieldInput)
        self.__state.addReference("price", priceFieldInput)

        mainBox.pack_start(serviceNameBox, False, False, 0)
        mainBox.pack_start(priceBox, False, False, 0)
        mainBox.pack_start(confirmButton, False, False, 0)

        return mainBox

    def __onConfirm(self, _: Gtk.Widget):
        pass

