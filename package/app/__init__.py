from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from package.Config import Config
from package.app.exception.DatabaseConnectionFailedException import DatabaseConnectionFailedException

if not Config.SQLALCHEMY_DB_URI: raise DatabaseConnectionFailedException

sqlalchemy_engine = create_engine(Config.SQLALCHEMY_DB_URI, echo=True)
sqlalchemy_base = declarative_base()

Session = sessionmaker(bind=sqlalchemy_engine)
sqlalchemy_session = Session()
