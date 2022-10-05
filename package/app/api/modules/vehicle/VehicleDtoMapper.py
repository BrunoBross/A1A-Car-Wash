from package.app.api.model.Vehicle import Vehicle
from package.app.api.modules.vehicle.dto.VehicleDto import VehicleDto
from package.app.meta.Singleton import Singleton


class VehicleDtoMapper(metaclass=Singleton):
    def mapVehicleToDto(self, vehicle: Vehicle) -> VehicleDto:
        return VehicleDto(id=vehicle.id, numberPlate=vehicle.numberPlate)

    def mapDtoToVehicle(self, dto: VehicleDto) -> Vehicle:
        return Vehicle(numberPlate=dto.numberPlate)
