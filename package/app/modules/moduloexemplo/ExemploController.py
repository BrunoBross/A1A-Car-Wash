from package.app.meta.Singleton import Singleton
from package.app.modules.moduloexemplo.ExemploService import ExemploService
from package.app.modules.moduloexemplo.ExemploView import ExemploView


class ExemploController(metaclass=Singleton):

    def __init__(self):
        self.__exemploService = ExemploService()
        self.__exemploView = ExemploView()

    def exemploHomeScreen(self):
        return self.__exemploView.showHomeScreen(
            self.__exemploService.getExampleInfo()
        )

    def unableToAccessModule(self):
        return self.__exemploView.unableToAccessModule()
