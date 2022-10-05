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

    def get(self) -> Gtk.Box:
        mainBox = Box(orientation=Gtk.Orientation.VERTICAL)

        label = Gtk.Label()
        label.set_markup(toBig("Cadastrar veiculos"))

        numberPlateFieldBox = Box(Gtk.Orientation.HORIZONTAL)
        numberPlateFieldLabel = Gtk.Label()
        numberPlateFieldInput = Gtk.Entry()
        numberPlateFieldLabel.set_text("Placa*")
        numberPlateFieldInput.set_margin_top(5)
        numberPlateFieldInput.set_margin_right(5)
        numberPlateFieldInput.set_margin_bottom(5)
        numberPlateFieldInput.set_margin_left(5)
        numberPlateFieldBox.pack_default(numberPlateFieldLabel)
        numberPlateFieldBox.pack_default(numberPlateFieldInput)

        confirmButton = Gtk.Button(label="Cadastrar")
        confirmButton.connect("clicked", self.__onConfirm)

        self.__numberPlateInput = numberPlateFieldInput

        mainBox.pack_start(label, False, False, 0)
        mainBox.pack_start(numberPlateFieldBox, False, False, 0)
        mainBox.pack_start(confirmButton, False, False, 0)

        return mainBox

    def __onConfirm(self, _: Gtk.Widget):
        self.__component.getState().addReference("numberPlate", self.__numberPlateInput)
        self.__component.requestCreateVehicle()
