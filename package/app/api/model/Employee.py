from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from package.Config import Config
from package.app import sqlalchemy_base
from package.app.api.model.User import User
from datetime import datetime

class Employee(sqlalchemy_base):

    __tablename__ = "tb_employee"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("tb_user.id"), nullable=False, unique=True)
    legal_name = Column(String(100), nullable=False)
    wage = Column(Float, default=Config.EMPLOYEE_WAGE_DEFAULT)
    active_register = Column(Boolean, nullable=False, default=True)
    job_limit = Column(
        Integer, nullable=False, default=Config.EMPLOYEE_MIN_JOBS_DEFAULT
    )
    admission_date = Column(Date, nullable=False, default=datetime.now().date())

    user = relationship(User)
