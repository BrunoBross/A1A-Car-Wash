from package.app.meta.Singleton import Singleton
from package.app.orm.Dao import Dao


class ExemploQuery(metaclass=Singleton):

    def __init__(self):
        self.__dao = Dao()

    def getExampleInfo(self) -> str:
        return "KKkKK to lombrado 🌿"
