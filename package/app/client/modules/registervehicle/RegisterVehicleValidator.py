import re
from package.app.meta.Singleton import Singleton

class RegisterVehicleValidator(metaclass=Singleton):
    def execute(self, numberPlate:str) -> bool:
        pattern = re.compile(r"[a-zA-Z]{3}\d(\d|[a-zA-Z]\d{2})")        
        return pattern.match(numberPlate)
