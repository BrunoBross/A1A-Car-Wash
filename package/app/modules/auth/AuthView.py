import PySimpleGUI as sg


class AuthView:
    def __init__(self):
        self.__window = None

    def open(self):
        div = [
            [sg.Text('Hello')],
            [sg.Button('Button', 1)]
        ]

        window = sg.Window('Base', element_justification='c', size=(700, 450)).Layout([
            [sg.Column(div, pad=(0, 50), element_justification='c')]
        ])

        self.__window = window
        button, values = self.__window.Read()
        self.__window.Close()
        return button
