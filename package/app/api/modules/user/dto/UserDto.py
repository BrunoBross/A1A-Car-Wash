from dataclasses import dataclass


@dataclass
class UserDto:
    id: int
    username: str
    passwordHash: bytes

