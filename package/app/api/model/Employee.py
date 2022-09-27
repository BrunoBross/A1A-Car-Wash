from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from package.Config import Config
from package.app import sqlalchemy_base
from package.app.api.model.User import User


class Employee(sqlalchemy_base):

    __tablename__ = "tb_employee"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("tb_user.id"), nullable=False, unique=True)
    legal_name = Column(String(100), nullable=False)
    wage = Column(Float, default=Config.EMPLOYEE_WAGE_DEFAULT)
    active_register = Column(Boolean, nullable=False, default=True)

    user = relationship(User)
