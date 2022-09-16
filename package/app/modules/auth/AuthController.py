from package.app.modules.auth.AuthView import AuthView


class AuthController:
    def __init__(self):
        self.__view = AuthView()

    def open_view(self):
        self.__view.open()
