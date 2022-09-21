from package.app.api.modules.auth.AuthController import AuthController
from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.client.modules.exemplo.ExemploComponent import ExemploComponent
from package.app.client.modules.login.LoginView import LoginView
from package.app.meta.Singleton import Singleton
from package.app.template.IAppComponent import IAppComponent


class LoginComponent(IAppComponent, metaclass=Singleton):

    def __init__(self):
        self.__view = LoginView()
        self.__authController = AuthController()

    def start(self):
        auth = self.__login()
        return ExemploComponent if auth else LoginComponent

    def __login(self):
        data = self.__view.getInfo()[1]
        dto = AuthDto(
            username=data[0],
            password=data[1]
        )

        return self.__authController.authenticate(dto)


