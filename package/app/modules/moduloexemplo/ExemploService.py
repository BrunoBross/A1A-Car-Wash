
from package.app.meta.Singleton import Singleton
from package.app.modules.moduloexemplo.ExemploQuery import ExemploQuery


class ExemploService(metaclass=Singleton):

    def __init__(self):
        self.__exemploQuery = ExemploQuery()

    def getExampleInfo(self):
        return self.__exemploQuery.getExampleInfo()
