from package.app.api.modules.vehicle.VehicleQuery import VehicleQuery
from package.app.api.modules.vehicle.dto.VehicleDto import VehicleDto
from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject


class VehicleValidator(metaclass=Singleton):
    def __init__(self) -> None:
        self.__query = VehicleQuery()

    @validator_function
    def execute(self, vehicleDto: VehicleDto, validation: ValidationObject) -> bool:
        if self.__query.getVehicleByNumberPlate(vehicleDto.numberPlate):
            validation.errors.add(
                f"Placa numérica '{vehicleDto.numberPlate}' já cadastrada. Por favor tente um valor diferente."
            )
            return False
        return True
