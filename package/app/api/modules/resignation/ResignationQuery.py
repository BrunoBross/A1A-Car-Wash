from typing import Optional
from package.app.api.model.Resignation import Resignation
from package.app.exception.DatabaseIntegrityException import DatabaseIntegrityException
from package.app.meta.Singleton import Singleton
from package.app.api.orm.DAO import DAO


class ResignationQuery(metaclass=Singleton):
    def __init__(self):
        self.__dao = DAO()

    def registerResignation(self, resignation: Resignation) -> Optional[Resignation]:
        try:
            self.__dao.insert(resignation)
            return resignation
        except DatabaseIntegrityException:
            return None
