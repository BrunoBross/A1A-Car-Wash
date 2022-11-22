from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from package.app.api.model.Employee import Employee
from package.app.api.model.Warning import Warning
from package.app import sqlalchemy_base


class WarningTable(sqlalchemy_base):

    __tablename__ = "tb_warning_table"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("tb_employee.id"), nullable=False, unique=True)
    warning_id = Column(Integer, ForeignKey("tb_warning.id"), nullable=False, unique=True)
    read = Column(Boolean, nullable=False, default=False)

    employee = relationship(Employee)
    warning = relationship(Warning)
