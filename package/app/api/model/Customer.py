from sqlalchemy import Column, Integer, String
from package.app import sqlalchemy_base


class Customer(sqlalchemy_base):

    __tablename__ = "tb_customer"

    id = Column(Integer, primary_key=True)
    cpf = Column(String(9), nullable=False, unique=True)
    legal_name = Column(String(100), nullable=False)
