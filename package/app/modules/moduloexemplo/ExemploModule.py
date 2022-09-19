
from package.app.meta.Singleton import Singleton
from package.app.modules.auth.AuthService import AuthService
from package.app.modules.moduloexemplo.ExemploController import ExemploController
from package.app.template.IAppModule import IAppModule


class ExemploModule(IAppModule, metaclass=Singleton):

    def __init__(self):
        self.__authService = AuthService()
        self.__exemploController = ExemploController()

    def start(self):
        while True:
            auth: bool = self.__authService.getAuthentication()
            if auth: self.__exemploController.exemploHomeScreen()
            else: self.__exemploController.unableToAccessModule()
