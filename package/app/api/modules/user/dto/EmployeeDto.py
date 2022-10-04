from dataclasses import dataclass
from typing import Optional


@dataclass
class EmployeeDto:
    id: Optional[int]
    user_id: Optional[int]
    legal_name: Optional[str]
    wage: Optional[str]
    active_register: Optional[bool]
