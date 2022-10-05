import re
from package.app.api.modules.vehicle.dto.VehicleDto import VehicleDto
from package.app.meta.Singleton import Singleton


class RegisterVehicleValidator(metaclass=Singleton):
    def execute(self, vehicleDto: VehicleDto) -> bool:
        pattern = re.compile(r"[a-zA-Z]{3}\d(\d|[a-zA-Z])\d{2}")
        return (
            bool(pattern.match(vehicleDto.numberPlate))
            if vehicleDto.numberPlate
            else False
        )
