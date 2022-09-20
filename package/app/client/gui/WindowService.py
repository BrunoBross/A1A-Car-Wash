from typing import Any
from PySimpleGUI import Button, Column, Window
from package.Config import Config
from package.app.meta.Singleton import Singleton


class WindowService(metaclass=Singleton):   # TODO: Portar para GTK

    @staticmethod
    def form(title: str, layout: list[Any], closeable: bool = False) -> tuple:
        input = WindowService.__open(title, layout, closeable)
        return input

    @staticmethod
    def message(title: str, layout: list[Any], closeable: bool = False) -> None:
        WindowService.__open(title, layout, closeable)

    @staticmethod
    def __makeCloseable(layout: list[Any]):
        layout.append(
        [Column([
            [Button(
                button_text=Config.CLOSE_BTN_TXT,
                key=Config.CLOSE_BTN_VAL
            )],
        ])])

    @staticmethod
    def __open(title: str, layout: list[Any], closeable: bool = False):
        if closeable: WindowService.__makeCloseable(layout)

        window = Window(
            f"{Config.APP_NAME} - {title}",
            element_justification='c',
            size=(
                Config.WINDOW_WIDTH,
                Config.WINDOW_HEIGHT
        )).Layout(layout)

        input = window.Read()
        window.Close()
        if Config.CLOSE_BTN_VAL in input:
            WindowService.__quit()
        return input

    @staticmethod
    def __quit(): exit(0)
