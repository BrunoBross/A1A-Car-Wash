from package.app.client.modules.login.LoginEventEnum import LoginEventEnum
from package.app.client.modules.login.LoginEventManager import LoginEventManager
from package.app.meta.Singleton import Singleton
from package.app.template.IAppModule import IAppModule
from package.app.client.gui.imports import Gtk


class Client(IAppModule, metaclass=Singleton):
    def __init__(self):
        self.__eventManager = LoginEventManager()

    def start(self):
        self.__eventManager.post(LoginEventEnum.STARTUP)
        Gtk.main()
