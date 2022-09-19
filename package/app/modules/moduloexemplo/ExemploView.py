from PySimpleGUI import Column, Text
from package.app.gui.WindowService import WindowService
from package.app.meta.Singleton import Singleton


class ExemploView(metaclass=Singleton):
    def __init__(self):
        self.__windowService = WindowService()

    def showHomeScreen(self, info):
        layout = [
            [Column([
                [Text(info)],
            ],
            pad=(0, 50),
            element_justification='c')
            ]
        ]
        self.__windowService.message('Home Screen', layout, closeable=True)

    def unableToAccessModule(self):
        layout = [
            [Column([
                [Text("garaio senhor white 💀")],
            ],
            pad=(0, 50),
            element_justification='c')
            ]
        ]
        self.__windowService.message('Unable to access module', layout, closeable=True)
