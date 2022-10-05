from package.app.meta.Singleton import Singleton
from package.app.api.modules.serviceregistration.serviceRegistrationService import serviceRegistrationService

class ServiceRegistrationController(metaclass=Singleton):

    def __init__(self):
        self.__serviceRegistrationService = serviceRegistrationService()

    def getExampleInfo(self) -> str:
        return self.__serviceRegistrationService.getExampleInfo()
