from package.app.api.crypt.utils import encrypt
from package.app.meta.Singleton import Singleton
from package.app.api.modules.user.UserService import UserService
from package.app.api.modules.employee.EmployeeController import EmployeeController


class RegisterEmployeeComponent(metaclass=Singleton):
    def __init__(self):
        self.__userService = UserService()
        self.__employeeController = EmployeeController()

    def registerEmployee(self, username: str, fullname: str, password: str, salary: str):
        if username == '' or fullname == '' or password == '' or salary == '':
            return print('\033[1;32m Preencha todos os campos!')
        if not salary.isnumeric():
            return print('\033[1;32m Digite um valor inteiro para o salário')
        if len(password) < 8 or len(password) > 255:
            return print('\033[1;32m Uma senha deve possuir no mínimo 8 e no máximo 255 caracteres')
        if self.__userService.getUserByUsername(username):
            return print('\033[1;32m Username já cadastrado')
        try:
            self.__employeeController.registerEmployee(username, fullname, encrypt(password), salary)
        except Exception as error:
            print(error)
        finally:
            print(f'\033[1;32m Funcionário {fullname} cadastrado com sucesso')
