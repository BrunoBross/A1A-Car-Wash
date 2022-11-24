import re
from package.app.api.modules.vehicle.dto.VehicleDto import VehicleDto
from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject


class RegisterVehicleValidator(metaclass=Singleton):
    @validator_function
    def execute(self, vehicleDto: VehicleDto, validation: ValidationObject) -> bool:
        pattern = re.compile(r"[a-zA-Z]{3}\d(\d|[a-zA-Z])\d{2}")
        print("***********************************************")
        print(vehicleDto)
        print(vehicleDto.numberPlate)
        if vehicleDto.numberPlate:
            valid = pattern.match(vehicleDto.numberPlate)
            if valid:
                return True
            validation.errors.add("Valor informado é inválido")
            return False

        validation.errors.add("Preencha todos os campos!")
        return False
