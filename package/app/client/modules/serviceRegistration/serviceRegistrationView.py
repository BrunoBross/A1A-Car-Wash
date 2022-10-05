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
        self.__service_name_input = Gtk.Widget
        self.__price_input = Gtk.Widget

    def get(self) -> Gtk.Box:

        mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        label = Gtk.Label()
        label.set_markup(toBig("Cadastrar Serviço"))
        label.set_margin_bottom(30)
        mainBox.pack_start(label, False, False, 0)

        serviceNameBox = Box(Gtk.Orientation.HORIZONTAL)
        serviceNameLabel = Gtk.Label()
        serviceNameLabel.set_text("Nome do serviço*")
        serviceNameLabel.set_margin_top(5)
        serviceNameLabel.set_margin_left(5)
        serviceNameLabel.set_margin_bottom(5)
        serviceNameLabel.set_margin_right(5)
        serviceNameBox.pack_default(serviceNameLabel)
        serviceNameInput = Gtk.Entry()
        serviceNameInput.set_margin_top(5)
        serviceNameInput.set_margin_left(5)
        serviceNameInput.set_margin_bottom(5)
        serviceNameInput.set_margin_right(5)
        serviceNameBox.pack_default(serviceNameInput)

        priceBox = Box(Gtk.Orientation.HORIZONTAL)
        priceLabel = Gtk.Label()
        priceLabel.set_text("Preço do serviço*")
        priceLabel.set_margin_top(5)
        priceLabel.set_margin_left(5)
        priceLabel.set_margin_bottom(5)
        priceLabel.set_margin_right(5)
        priceBox.pack_default(priceLabel)
        priceInput = Gtk.Entry()
        priceInput.set_margin_top(5)
        priceInput.set_margin_left(5)
        priceInput.set_margin_bottom(5)
        priceInput.set_margin_right(5)
        priceBox.pack_default(priceInput)    

        confirmButton = Gtk.Button(label="Cadastrar")
        confirmButton.set_margin_top(30)
        confirmButton.connect("clicked", self.__onConfirm)

        self.__service_name_input = serviceNameInput
        self.__price_input = priceInput

        mainBox.pack_start(serviceNameBox, False, False, 0)
        mainBox.pack_start(priceBox, False, False, 0)
        mainBox.pack_start(confirmButton, False, False, 0)

        return mainBox

    def __onConfirm(self, _: Gtk.Widget):
        self.__component.getState().addReference("service_name", self.__service_name_input)
        self.__component.getState().addReference("price", self.__price_input)
        self.__component.serviceRegistration()
