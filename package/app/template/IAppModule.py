from abc import abstractmethod


class IAppModule:

    @abstractmethod
    def start() -> None: pass

