from enum import Enum
import os


class Config:
    APP_NAME = "A1A Carwash"
    SQLALCHEMY_DB_URI = os.environ.get("A1A_DATABASE")
    ENCODING = "utf-8"
    CLOSE_BTN_TXT = "Fechar"
    CLOSE_BTN_VAL = "CLOSE"
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 700
    SIDEBAR_WIDTH = 350
    BORDER_WIDTH = 10
    GTK_VERSION = "3.0"
    EMPLOYEE_WAGE_DEFAULT = 1000
    LOG_OUT = print

    class CommandLineArgument(Enum):
        APP = "app"
        DATABASE = "database"
