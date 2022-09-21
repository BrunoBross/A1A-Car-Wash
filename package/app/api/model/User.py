from sqlalchemy import Column, Integer, String
from package.app import sqlalchemy_base


class User(sqlalchemy_base):

    __tablename__ = "tb_user"

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
