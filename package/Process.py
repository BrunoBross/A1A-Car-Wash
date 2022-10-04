from typing import Protocol


class Process(Protocol):
    @staticmethod
    def start() -> None:
        ...
