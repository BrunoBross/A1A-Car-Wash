from typing import Type
from package.Process import Process
from package.app.client.Client import Client
from package.app.template.IAppModule import IAppModule

STARTER_MODULE: Type[IAppModule] = Client


class App(Process):
    @staticmethod
    def start():
        STARTER_MODULE().start()
