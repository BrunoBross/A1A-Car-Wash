from package.app.meta.Singleton import Singleton
from package.app.api.modules.service.serviceQuery import ServiceQuery


class ServiceService(metaclass=Singleton):

    def __init__(self):
        self.__serviceQuery = ServiceQuery()

    def getExampleInfo(self) -> str:
        return self.__serviceQuery.getExampleInfo()

    def serviceRegistration(self, service_name: str, price: str):
        self.__serviceQuery.serviceRegistration(service_name, price)
