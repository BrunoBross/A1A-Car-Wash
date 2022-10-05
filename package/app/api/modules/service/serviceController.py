from package.app.meta.Singleton import Singleton
from package.app.api.modules.service.serviceService import ServiceService

class ServiceController(metaclass=Singleton):

    def __init__(self):
        self.__serviceService = ServiceService()

    def getExampleInfo(self) -> str:
        return self.__serviceService.getExampleInfo()

    def serviceRegistrastion(self, service_name, price):
        self.__serviceService.serviceRegistration(service_name, price)