from sqlalchemy import Column, Integer, String
from package.app import sqlalchemy_base


class SchedulingState(sqlalchemy_base):

    __tablename__ = "tb_scheduling_state"

    id = Column(Integer, primary_key=True)
    description = Column(String(100), nullable=False, unique=True)
