from package.app.meta.Singleton import Singleton


class UserContext(metaclass=Singleton):
    pass

    def isAuthenticated(self) -> bool:
        return False
