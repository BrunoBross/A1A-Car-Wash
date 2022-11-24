from sqlalchemy import Column, Integer, String, Date
from package.app import sqlalchemy_base


class Warning(sqlalchemy_base):

    __tablename__ = "tb_warning"

    id = Column(Integer, primary_key=True)
    description = Column(String(256), nullable=False)
    date = Column(Date, nullable=False)
