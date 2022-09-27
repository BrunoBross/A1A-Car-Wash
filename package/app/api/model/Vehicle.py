from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from package.app import sqlalchemy_base
from package.app.api.model.Customer import Customer


class Vehicle(sqlalchemy_base):

    __tablename__ = "tb_vehicle"

    id = Column(Integer, primary_key=True)
    numberPlate = Column(String(20), nullable=False, unique=True)
    owner_id = Column(Integer, ForeignKey("tb_customer.id"))

    owner = relationship(Customer)
