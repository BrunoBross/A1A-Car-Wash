from dataclasses import dataclass


@dataclass
class AuthDto:
    username: str
    password: str
