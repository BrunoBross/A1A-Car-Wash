from dataclasses import dataclass, field
from typing import Optional
from datetime import date
from package.app.api.model.Employee import Employee
from package.app.api.model.ResignationType import ResignationType

@dataclass
class ResignationDto:
    id: Optional[int] = field(default=None)
    employee_id: Optional[int] = field(default=None)
    resignation_type_id: Optional[int] = field(default=None)
    date: Optional[date] = field(default=None)
    memo: Optional[str] = field(default=None)
    employee: Optional[Employee] = field(default=None)
    resignation_type: Optional[ResignationType] = field(default=None)
