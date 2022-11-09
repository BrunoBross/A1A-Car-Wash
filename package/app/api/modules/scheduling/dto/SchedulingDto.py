from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from package.app.api.enum.SchedulingStateEnum import SchedulingStateEnum

from package.app.api.modules.employee.dto.EmployeeDto import EmployeeDto
from package.app.api.modules.job.dto.JobDto import JobDto
from package.app.api.modules.vehicle.dto.VehicleDto import VehicleDto


@dataclass
class SchedulingDto:
    employee: Optional[EmployeeDto] = field(default=None)
    job: Optional[JobDto] = field(default=None)
    vehicle: Optional[VehicleDto] = field(default=None)
    job_state: Optional[SchedulingStateEnum] = field(default=None)
    date: Optional[datetime.date] = field(default=None)
