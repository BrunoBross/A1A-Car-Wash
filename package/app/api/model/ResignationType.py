from sqlalchemy import Column, Integer, String
from package.app import sqlalchemy_base


class ResignationType(sqlalchemy_base):

    __tablename__ = "tb_resignation_type"

    id = Column(Integer, primary_key=True)
    description = Column(String(50), nullable=False, unique=True)
