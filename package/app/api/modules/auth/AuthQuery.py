from package.app.meta.Singleton import Singleton


class AuthQuery(metaclass=Singleton):

    def __init__(self):
        pass

    def authenticate(self, info):
        return True
