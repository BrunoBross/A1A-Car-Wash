from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from package.app import sqlalchemy_base
from package.app.api.model.Employee import Employee
from package.app.api.model.ResignationType import ResignationType


class Resignation(sqlalchemy_base):

    __tablename__ = "tb_resignation"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("tb_employee.id"), nullable=False)
    resignation_type_id = Column(
        Integer, ForeignKey("tb_resignation_type.id"), nullable=False
    )
    date = Column(Date, nullable=False)
    memo = Column(String(256), nullable=True)

    employee = relationship(Employee)
    resignation_type = relationship(ResignationType)
