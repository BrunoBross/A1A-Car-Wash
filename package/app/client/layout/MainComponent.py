from package.app.client.state.UserContext import UserContext
from package.app.meta.Singleton import Singleton


class MainComponent(metaclass=Singleton):
    def __init__(self):
        self.__userContext = UserContext()

    def getUserContext(self):
        return self.__userContext
