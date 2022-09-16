from PySimpleGUI import Button, Column, Text
from package.app.gui.WindowService import WindowService


class AuthView:

    @staticmethod
    def login():

        layout = [
            [Column([
                [Text('Hello')],
                [Button('OK')]
            ],
            pad=(0, 50),
            element_justification='c')
            ]
        ]
        val = WindowService.form('Auth', layout)

        return val
