from PySimpleGUI import Button, Column, InputText, Text
from package.app.client.gui.WindowService import WindowService
from package.app.meta.Singleton import Singleton


class LoginView(metaclass=Singleton):

    def __init__(self):
        self.__windowService = WindowService()

    def getInfo(self):

        layout = [
            [Column([
                [Text('Login')],
                [Text('username', size =(15, 1)), InputText()],
                [Text('password', size =(15, 1)), InputText()],
                [Button('OK')],
            ],
            pad=(0, 50),
            element_justification='c')
            ]
        ]
        val = self.__windowService.form('Auth', layout)

        return val
