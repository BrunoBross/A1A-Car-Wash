from dataclasses import dataclass

from package.app.api.enum.RoleEnum import RoleEnum


@dataclass
class UserDto:
    id: int
    username: str
    role: RoleEnum
