from sqlalchemy import Column, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship
from package.app import sqlalchemy_base
from package.app.api.model.Employee import Employee
from package.app.api.model.Job import Job
from package.app.api.model.SchedulingState import SchedulingState
from package.app.api.model.Vehicle import Vehicle


class Scheduling(sqlalchemy_base):

    __tablename__ = "tb_scheduling"

    employee_id = Column(Integer, ForeignKey("tb_employee.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("tb_job.id"), primary_key=True)
    vehicle_id = Column(Integer, ForeignKey("tb_vehicle.id"), primary_key=True)
    date = Column(Date, primary_key=True)
    job_state_id = Column(Integer, ForeignKey("tb_scheduling_state.id"))

    employee = relationship(Employee)
    job = relationship(Job)
    vehicle = relationship(Vehicle)
    job_state = relationship(SchedulingState)
