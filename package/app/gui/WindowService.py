from typing import Any
from PySimpleGUI import Button, Column, Window
from package.Config import Config
from package.app.meta.Singleton import Singleton


class WindowService(metaclass=Singleton):   # TODO: refactor

    @staticmethod
    def form(title: str, layout: list[Any], closeable: bool = False) -> Any:
        if closeable:
            layout.append(
            [Column([
                [Button(Config.CLOSE_BTN_TXT)],
            ])])

        window = Window(
            f"{Config.APP_NAME} - {title}",
            element_justification='c',
            size=(
                Config.WINDOW_WIDTH,
                Config.WINDOW_HEIGHT
        )).Layout(layout)

        input = window.Read()
        window.Close()
        return input

    @staticmethod
    def message(title: str, layout: list[Any], closeable: bool = False) -> None:
        if closeable:
            layout.append(
            [Column([
                [Button(Config.CLOSE_BTN_TXT)],
            ])])

        window = Window(
            f"{Config.APP_NAME} - {title}",
            element_justification='c',
            size=(
                Config.WINDOW_WIDTH,
                Config.WINDOW_HEIGHT
        )).Layout(layout)

        window.Read()
        window.Close()
