from dataclasses import dataclass, field
from typing import Optional


@dataclass
class EmployeeDto:
    id: Optional[int] = field(default=None)
    user_id: Optional[int] = field(default=None)
    legal_name: Optional[str] = field(default=None)
    wage: Optional[str] = field(default=None)
    active_register: Optional[bool] = field(default=None)
