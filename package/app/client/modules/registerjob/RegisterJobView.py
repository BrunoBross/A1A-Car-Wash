from package.app.client.modules.registerjob.RegisterJobComponent import (
    RegisterJobComponent,
)
from package.app.meta.Singleton import Singleton
from package.app.client.utils.markup import toBig
from package.app.client.gui.box.Box import Box
from package.app.client.gui.imports import Gtk


class RegisterJobView(metaclass=Singleton):
    def __init__(self):
        self.__component = RegisterJobComponent()
        self.__jobNameInput = Gtk.Widget
        self.__jobValueInput = Gtk.Widget

    def get(self) -> Gtk.Box:

        mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        label = Gtk.Label()
        label.set_markup(toBig("Cadastrar Serviço"))
        label.set_margin_bottom(30)

        jobNameBox = Box(Gtk.Orientation.HORIZONTAL)
        jobNameLabel = Gtk.Label()
        jobNameLabel.set_text("Nome do serviço*")
        jobNameLabel.set_margin_top(5)
        jobNameLabel.set_margin_left(5)
        jobNameLabel.set_margin_bottom(5)
        jobNameLabel.set_margin_right(5)
        jobNameBox.pack_default(jobNameLabel)
        jobNameInput = Gtk.Entry()
        jobNameInput.set_margin_top(5)
        jobNameInput.set_margin_left(5)
        jobNameInput.set_margin_bottom(5)
        jobNameInput.set_margin_right(5)
        jobNameBox.pack_default(jobNameInput)

        jobValueBox = Box(Gtk.Orientation.HORIZONTAL)
        jobValueLabel = Gtk.Label()
        jobValueLabel.set_text("Preço do serviço*")
        jobValueLabel.set_margin_top(5)
        jobValueLabel.set_margin_left(5)
        jobValueLabel.set_margin_bottom(5)
        jobValueLabel.set_margin_right(5)
        jobValueBox.pack_default(jobValueLabel)
        jobValueInput = Gtk.Entry()
        jobValueInput.set_margin_top(5)
        jobValueInput.set_margin_left(5)
        jobValueInput.set_margin_bottom(5)
        jobValueInput.set_margin_right(5)
        jobValueBox.pack_default(jobValueInput)

        confirmButton = Gtk.Button(label="Cadastrar")
        confirmButton.set_margin_top(30)
        confirmButton.connect("clicked", self.__onConfirm)

        self.__jobNameInput = jobNameInput
        self.__jobValueInput = jobValueInput

        mainBox.pack_start(label, False, False, 0)
        mainBox.pack_start(jobNameBox, False, False, 0)
        mainBox.pack_start(jobValueBox, False, False, 0)
        mainBox.pack_start(confirmButton, False, False, 0)

        return mainBox

    def __onConfirm(self, _: Gtk.Widget):
        self.__component.getState().addReference("jobName", self.__jobNameInput)
        self.__component.getState().addReference("jobValue", self.__jobValueInput)

        self.__component.requestRegistration()
