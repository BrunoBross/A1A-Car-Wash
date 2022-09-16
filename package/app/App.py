from package.Process import Process
from package.app.modules.auth.AuthService import AuthService


class App(Process):

    @staticmethod
    def start():
        AuthService.start()
