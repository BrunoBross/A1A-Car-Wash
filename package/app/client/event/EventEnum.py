from enum import Enum, auto


class EventEnum(Enum):
    STARTUP = auto()
    LOGIN = auto()
    LOGOUT = auto()
    CONTEXT_SET = auto()
    SWITCH_VIEW = auto()
    WINDOW_OPENED = auto()
    WINDOW_CLOSED = auto()
    VALIDATION = auto()
