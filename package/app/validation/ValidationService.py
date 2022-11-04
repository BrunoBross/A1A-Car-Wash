from package.app.client.event.EventEnum import EventEnum
from package.app.client.event.EventManager import EventManager
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject


class ValidationService(metaclass=Singleton):
    def __init__(self):
        self.__eventManager = EventManager()

    def post(self, validationObject: ValidationObject):
        self.__eventManager.post(EventEnum.VALIDATION, validationObject)
