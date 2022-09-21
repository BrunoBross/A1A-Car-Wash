from package.app.api.model.User import User
from package.app.api.modules.auth.dto.AuthDto import AuthDto
from package.app.api.orm.DAO import DAO
from package.app.meta.Singleton import Singleton


class AuthQuery(metaclass=Singleton):

    def __init__(self):
        self.__dao = DAO()
