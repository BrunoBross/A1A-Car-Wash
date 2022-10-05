from package.app.client.gui.box.Box import Box
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk
from package.app.client.utils.markup import toBig
from package.app.client.state.ComponentState import ComponentState

class RegisterVehicleView(metaclass=Singleton):
    def __init__(self):
        self.__component = RegisterVehicleComponent()
        self.__state = ComponentState

    def get(self) -> Gtk.Box:
        mainBox = Box(orientation=Gtk.Orientation.VERTICAL)
        label = Gtk.Label()
        label.set_markup(toBig("Cadastrar veiculos"))
        mainBox.pack_start(label, False, False, 0)

        boardFieldBox = Box(Gtk.Orientation.HORIZONTAL)
        boardFieldLabel = Gtk.Label()
        boardFieldInput = Gtk.Entry()
        boardFieldLabel.set_text("Placa*")
        boardFieldInput.set_margin_top(5)
        boardFieldInput.set_margin_right(5)
        boardieldInput.set_margin_bottom(5)
        boardFieldInput.set_margin_left(5)
        boardFieldBox.pack_default(boardFieldLabel)
        boardFieldBox.pack_default(boardFieldInput)

        

        confirmButton = Gtk.Button(label="Cadastrar")
        confirmButton.connect("clicked", self.__onConfirm)

        self.__component.getState().addReference("board", boardFieldInput)

        mainBox.pack_start(boardFieldBox, False, False, 0)
        mainBox.pack_start(confirmButton, False, False, 0)

        return mainBox

    def __onConfirm(self, _: Gtk.Widget):
        self.__component.createVehicle(
            Gtk.EntryBuffer.get_text(self.__state.getReferenceById("board"))
        )
