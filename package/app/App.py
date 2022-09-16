from package.app.modules.auth.AuthController import AuthController


class App:
    def __init__(self):
        self.__auth_controller = AuthController()
        return

    def start(self):
        self.open_initial_view()

    def open_initial_view(self):
        self.__auth_controller.open_view()
