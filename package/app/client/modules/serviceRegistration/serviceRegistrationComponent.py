from package.app.api.modules.serviceregistration.serviceRegistrationController import serviceRegistrationController
from package.app.meta.Singleton import Singleton


class ServiceRegistrationComponent(metaclass=Singleton):
    def __init__(self):
        self.__exemploController = serviceRegistrationController()

    def getText(self) -> str:
        return self.__exemploController.getExampleInfo()
