from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO


class ExemploQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()

    def getExampleInfo(self) -> str:
        return "KKkKK to lombrado 🌿"
