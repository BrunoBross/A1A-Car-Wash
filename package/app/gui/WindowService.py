from typing import Any
from PySimpleGUI import Window
from package.Config import Config


class WindowService:

    @staticmethod
    def form(title: str, layout: list[Any]) -> Any:
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
    def message() -> None:
        pass
