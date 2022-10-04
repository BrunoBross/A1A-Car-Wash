from package.app.meta.Singleton import Singleton
from package.app.api.modules.user.UserService import UserService


class RegisterEmployeeComponent(metaclass=Singleton):
    def __init__(self):
        self.__userService = UserService()

    def registerEmployee(self, username: str, fullname: str, password: str, salary: str):
        if username == '' or fullname == '' or password == '' or salary == '':
            return print('Preencha todos os campos!')
        else:
            if not salary.isnumeric():
                return print('Digite um valor inteiro para o salário')
            self.__userService.createEmployee(username, fullname, password, salary)
