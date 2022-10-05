from dataclasses import dataclass, field
from typing import Optional

from package.app.api.enum.RoleEnum import RoleEnum


@dataclass
class UserDto:
    id: Optional[int] = field(default=None)
    username: Optional[str] = field(default=None)
    role: Optional[RoleEnum] = field(default=None)
