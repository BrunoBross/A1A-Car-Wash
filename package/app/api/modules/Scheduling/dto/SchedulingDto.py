from dataclasses import dataclass, field
from typing import Optional
from datetime import date
from sqlalchemy import Date
#from package.app.api.modules.user.dto.UserDto import UserDto


@dataclass
class SchedulingDto:
    employee_id: Optional[int] = field(default=None)  
    job_id: Optional[int]= field(default=None)  
    vehicle_id:  Optional[int]= field(default=None)  
    date: Optional[Date]= field(default=None)  
    job_state_id: Optional[int] = field(default=None)  
    
