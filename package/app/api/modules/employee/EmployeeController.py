from package.app.api.modules.employee.EmployeeService import EmployeeService
from package.app.api.modules.user.UserService import UserService
from package.app.api.crypt.utils import encrypt
from package.app.meta.Singleton import Singleton


class EmployeeController(metaclass=Singleton):
    def __init__(self):
        self.__userService = UserService()
        self.__employeeService = EmployeeService()

    def registerEmployeeQuery(self, username: str, fullname: str, password: str, salary: str):
        self.__employeeService.registerEmployee(username, fullname, password, salary)

    def getEmployeeFullNameByUsername(self, username: str):
        return self.__employeeService.getEmployeeFullNameByUsername(username)

    def registerEmployee(self, username: str, fullname: str, password: str, salary: str):
        if not (self.validateNullFields(username, fullname, password, salary) and
                self.validateSalary(salary) and
                self.validatePassword(password) and
                self.validateHasUsername(username)):
            return
        try:
            self.registerEmployeeQuery(username, fullname, encrypt(password), salary)
        except Exception as error:
            print(error)
        finally:
            print(f'\033[1;32m Funcionário {fullname} cadastrado com sucesso \033[0m')

    def validateNullFields(self, username: str, fullname: str, password: str, salary: str):
        if username == '' or fullname == '' or password == '' or salary == '':
            print('\033[1;91m Preencha todos os campos!')
            return False
        return True

    def validateSalary(self, salary: str):
        if not salary.isnumeric() or int(salary) < 1000:
            print('\033[1;91m Digite um valor inteiro para o salário \033[0m')
            return False
        return True

    def validatePassword(self, password: str):
        if len(password) < 8 or len(password) > 255:
            print('\033[1;91m Uma senha deve possuir no mínimo 8 e no máximo 255 caracteres \033[0m')
            return False
        return True

    def validateHasUsername(self, username: str):
        if self.__userService.getUserByUsername(username):
            print('\033[1;91m Username já cadastrado \033[0m')
            return False
        return True
