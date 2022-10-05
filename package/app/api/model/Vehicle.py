from sqlalchemy import Column, ForeignKey, Integer, String
from package.app import sqlalchemy_base


class Vehicle(sqlalchemy_base):

    __tablename__ = "tb_vehicle"

    id = Column(Integer, primary_key=True)
    numberPlate = Column(String(20), nullable=False, unique=True)
