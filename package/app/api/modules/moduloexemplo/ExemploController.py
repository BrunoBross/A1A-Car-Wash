from package.app.meta.Singleton import Singleton
from package.app.api.modules.moduloexemplo.ExemploService import ExemploService


class ExemploController(metaclass=Singleton):

    def __init__(self):
        self.__exemploService = ExemploService()

    def getExampleInfo(self) -> str:
        return self.__exemploService.getExampleInfo()
