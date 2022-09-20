from typing import Type
from package.Process import Process
from package.app.client.Client import Client
from package.app.template.IAppModule import IAppModule

INITIAL_MODULE: Type[IAppModule] = Client

class App(Process):

    @staticmethod
    def start():
        INITIAL_MODULE().start()
