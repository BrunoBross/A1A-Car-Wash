from dataclasses import dataclass
from typing import Optional

from package.app.api.enum.RoleEnum import RoleEnum


@dataclass
class UserDto:
    id: Optional[int]
    username: Optional[str]
    role: Optional[RoleEnum]
