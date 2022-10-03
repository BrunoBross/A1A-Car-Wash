from package.app.api.modules.moduloexemplo.ExemploController import ExemploController
from package.app.meta.Singleton import Singleton


class ExemploComponent(metaclass=Singleton):
    def __init__(self):
        self.__exemploController = ExemploController()

    def getText(self) -> str:
        return self.__exemploController.getExampleInfo()
