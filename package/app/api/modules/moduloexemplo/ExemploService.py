from package.app.meta.Singleton import Singleton
from package.app.api.modules.moduloexemplo.ExemploQuery import ExemploQuery


class ExemploService(metaclass=Singleton):
    def __init__(self):
        self.__exemploQuery = ExemploQuery()

    def getExampleInfo(self) -> str:
        return self.__exemploQuery.getExampleInfo()
