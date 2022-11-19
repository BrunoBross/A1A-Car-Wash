from dataclasses import dataclass, field
from typing import Optional
from package.app.api.modules.user.dto.UserDto import UserDto
from sqlalchemy import Date


@dataclass
class EmployeeDto:
    id: Optional[int] = field(default=None)
    user: Optional[UserDto] = field(default=None)
    legalName: Optional[str] = field(default=None)
    wage: Optional[str] = field(default=None)
    activeRegister: Optional[bool] = field(default=None)
    jobLimit: Optional[str] = field(default=None)
    admission_date: Optional[Date] = field(default=None)
