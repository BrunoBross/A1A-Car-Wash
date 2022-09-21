import bcrypt

from package.Process import Process
from package.Config import Config
from package.app.exception.DatabaseConnectionFailedException import DatabaseConnectionFailedException
from package.app.api.crypt.utils import encrypt
from package.app import sqlalchemy_base, sqlalchemy_engine, sqlalchemy_session

from package.database.imports import *

class Database(Process):

    @staticmethod
    def start():
        Database.__dropAll()
        Database.__creaeteAll()
        Database.__migrate()

    @staticmethod
    def __dropAll():
        sqlalchemy_base.metadata.drop_all(sqlalchemy_engine)
        sqlalchemy_session.commit()

    @staticmethod
    def __creaeteAll():
        sqlalchemy_base.metadata.create_all(sqlalchemy_engine)
        sqlalchemy_session.commit()

    @staticmethod
    def __migrate():
        sqlalchemy_session.add(User(
            username="admin",
            password=encrypt("senha")
        ))

        sqlalchemy_session.commit()

