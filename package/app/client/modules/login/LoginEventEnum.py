from enum import Enum, auto


class LoginEventEnum(Enum):
    STARTUP = auto()
    LOGIN = auto()
    LOGOUT = auto()
