from package.app.api.modules.moduloexemplo.ExemploController import ExemploController
from package.app.client.modules.exemplo.ExemploView import ExemploView
from package.app.meta.Singleton import Singleton
from package.app.template.IAppComponent import IAppComponent


class ExemploComponent(IAppComponent, metaclass=Singleton):

    def __init__(self):
        self.__exemploController = ExemploController()
        self.__view = ExemploView()

    def start(self):
        data = self.__exemploController.getExampleInfo()
        self.__view.showHomeScreen(data)
