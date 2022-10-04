from random import random
from package.app.client.gui.box.Box import Box
from package.app.client.modules.login.LoginComponent import LoginComponent
from package.app.meta.Singleton import Singleton
from package.app.client.gui.imports import Gtk
from package.app.client.utils.markup import toBig


class LoginView(metaclass=Singleton):
    def __init__(self):
        self.__component = LoginComponent()

    def get(self) -> Gtk.Box:
        mainBox = Box(orientation=Gtk.Orientation.VERTICAL)
        label = Gtk.Label()
        label.set_markup(toBig("Login"))
        mainBox.pack_start(label, False, False, 0)

        usernameFieldBox = Box(Gtk.Orientation.HORIZONTAL)
        usernameFieldLabel = Gtk.Label()
        usernameFieldInput = Gtk.Entry()
        usernameFieldLabel.set_text("Username")
        usernameFieldInput.set_margin_top(5)
        usernameFieldInput.set_margin_right(5)
        usernameFieldInput.set_margin_bottom(5)
        usernameFieldInput.set_margin_left(5)
        usernameFieldBox.pack_default(usernameFieldLabel)
        usernameFieldBox.pack_default(usernameFieldInput)

        passwordFieldBox = Box(Gtk.Orientation.HORIZONTAL)
        passwordFieldLabel = Gtk.Label()
        passwordFieldInput = Gtk.Entry()
        passwordFieldInput.set_visibility(False)
        passwordFieldLabel.set_text("Password")
        passwordFieldInput.set_margin_top(5)
        passwordFieldInput.set_margin_right(5)
        passwordFieldInput.set_margin_bottom(5)
        passwordFieldInput.set_margin_left(5)
        passwordFieldBox.pack_default(passwordFieldLabel)
        passwordFieldBox.pack_default(passwordFieldInput)

        confirmButton = Gtk.Button(label="Confirm")
        confirmButton.connect("clicked", self.__onConfirm)

        self.__component.getState().addReference("username", usernameFieldInput)
        self.__component.getState().addReference("password", passwordFieldInput)

        mainBox.pack_default(usernameFieldBox)
        mainBox.pack_default(passwordFieldBox)
        mainBox.pack_default(confirmButton)

        return mainBox

    def __onConfirm(self, _: Gtk.Widget):
        self.__component.requestAuth()
