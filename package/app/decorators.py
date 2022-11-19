from collections.abc import Callable
from package.app.client.event.EventEnum import EventEnum
from package.app.client.event.EventManager import EventManager
from package.app.exception.DatabaseIntegrityException import DatabaseIntegrityException
from package.app import sqlalchemy_session
from package.app.validation.ValidationObject import ValidationObject
from package.app.validation.ValidationService import ValidationService


def safe_query(transaction: Callable):
    def wrapper(*args, **kwargs):
        try:
            return transaction(*args, **kwargs)
        except Exception:
            sqlalchemy_session.rollback()
            raise DatabaseIntegrityException

    return wrapper


def validator_function(callback):
    validationService = ValidationService()

    def wrapper(*args, **kwargs):
        validation = ValidationObject()
        result = callback(validation=validation, *args, **kwargs)
        validationService.post(validation)
        return result

    return wrapper


def post_endpoint(callback):
    eventManager = EventManager()

    def wrapper(*args, **kwargs):
        result = callback(*args, **kwargs)
        if result:
            eventManager.post(EventEnum.SUBMIT_SUCCESS)
        else:
            eventManager.post(EventEnum.SUBMIT_FAILED)
        return result

    return wrapper
