import os


class Config:
    APP_NAME = "A1A Carwash"
    SQLALCHEMY_DB_URI = os.environ.get('A1A_DATABASE')
    ENCODING = 'utf-8'
    CLOSE_BTN_TXT = "Fechar"
    CLOSE_BTN_VAL = "CLOSE"
    WINDOW_WIDTH = 700
    WINDOW_HEIGHT = 450
    OPTION_DATABASE = "database"
    OPTION_APP = "app"
    OPTIONS = { OPTION_APP, OPTION_DATABASE }
