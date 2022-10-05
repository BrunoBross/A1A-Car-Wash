from package.app import sqlalchemy_base, sqlalchemy_engine, sqlalchemy_session

from package.database.imports import *
from package.database.migration import createMigration


class Database:
    @staticmethod
    def start():
        Database.__dropAll()
        Database.__createAll()
        Database.__migrate()

    @staticmethod
    def __dropAll():
        sqlalchemy_base.metadata.drop_all(sqlalchemy_engine)
        sqlalchemy_session.commit()

    @staticmethod
    def __createAll():
        sqlalchemy_base.metadata.create_all(sqlalchemy_engine)
        sqlalchemy_session.commit()

    @staticmethod
    def __migrate():
        migrations = createMigration()
        for element in migrations:
            sqlalchemy_session.add(element)
        sqlalchemy_session.commit()
