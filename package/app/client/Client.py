from typing import Any, Optional, Type
from package.app.client.modules.login.LoginComponent import LoginComponent
from package.app.meta.Singleton import Singleton
from package.app.template.IAppComponent import IAppComponent
from package.app.template.IAppModule import IAppModule


class Client(IAppModule, metaclass=Singleton):


    def __init__(self):
        self.__component: Optional[Type[IAppComponent]] = LoginComponent

    def start(self):
        while True:
            if not self.__component: exit(0)
            self.__component = self.__component().start()

