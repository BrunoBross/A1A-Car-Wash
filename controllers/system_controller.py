from controllers.auth_controller import AuthController


class SystemController:
    def __init__(self):
        self.__auth_controller = AuthController()
        return

    def start_system(self):
        self.open_initial_view()

    def open_initial_view(self):
        self.__auth_controller.open_view()
