from PySimpleGUI import Button, Column, Text
from package.app.client.gui.WindowService import WindowService
from package.app.meta.Singleton import Singleton


class LoginView(metaclass=Singleton):

    def __init__(self):
        self.__windowService = WindowService()

    def getInfo(self):

        layout = [
            [Column([
                [Text('Login')],
                [Button('OK')],
                [Button('NAO OK')]
            ],
            pad=(0, 50),
            element_justification='c')
            ]
        ]
        val = self.__windowService.form('Auth', layout, closeable=True)

        return val
