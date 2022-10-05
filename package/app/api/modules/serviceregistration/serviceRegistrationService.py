from package.app.meta.Singleton import Singleton
from package.app.api.modules.serviceregistration.serviceRegistrationQuery import serviceRegistrationQuery


class serviceRegistrationService(metaclass=Singleton):

    def __init__(self):
        self.__serviceRegistrationQuery = serviceRegistrationQuery()

    def getExampleInfo(self) -> str:
        return self.__serviceRegistrationQuery.getExampleInfo()
