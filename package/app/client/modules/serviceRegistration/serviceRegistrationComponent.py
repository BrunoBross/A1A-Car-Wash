from package.app.api.modules.service.serviceController import ServiceController
from package.app.meta.Singleton import Singleton


class ServiceRegistrationComponent(metaclass=Singleton):
    def __init__(self):
        self.__serviceRegistrationController = ServiceController()

    def getText(self) -> str:
        return self.__serviceRegistrationController.getExampleInfo()

    def serviceRegistration(self, service_name: str, price: str):
        if service_name == '' or price == '':
            return print('Preencha todos os campos!')
        if not price.isnumeric():
            return print('O campo preço deve conter um valor numérico!')
        try:
            self.__serviceRegistrationController.serviceRegistrastion(service_name, price)
            print('Serviço {service_name} cadastrado com sucesso')
        except Exception as error:
            print(error)
