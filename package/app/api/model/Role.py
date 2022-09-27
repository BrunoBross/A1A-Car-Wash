from sqlalchemy import Column, Integer, String
from package.app import sqlalchemy_base


class Role(sqlalchemy_base):

    __tablename__ = "tb_role"

    id = Column(Integer, primary_key=True)
    description = Column(String(20), unique=True, nullable=False)
