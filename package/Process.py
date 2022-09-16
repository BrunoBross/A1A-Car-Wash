from abc import ABC, abstractmethod


class Process(ABC):

    @abstractmethod
    def start() -> None: pass

