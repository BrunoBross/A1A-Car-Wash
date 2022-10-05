from package.app.api.model.Job import Job
from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO


class ServiceQuery(metaclass=Singleton):

    def __init__(self):
        self.__dao = DAO()

    def getExampleInfo(self) -> str:
        return "KKkKK to lombrado 🌿"

    def serviceRegistration(self, service_name: str, price: str):
        self.__dao.insert(Job(description=service_name, cost_value=price))
