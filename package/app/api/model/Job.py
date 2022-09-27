from sqlalchemy import Column, Float, Integer, String
from package.app import sqlalchemy_base


class Job(sqlalchemy_base):

    __tablename__ = "tb_job"

    id = Column(Integer, primary_key=True)
    description = Column(String(100), unique=True, nullable=False)
    cost_value = Column(Float, nullable=False)
