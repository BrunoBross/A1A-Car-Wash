from package.app.api.model.Job import Job
from package.app.api.modules.service.dto.serviceDto import ServiceDto
from package.app.meta.Singleton import Singleton


class VehicleDtoMapper(metaclass=Singleton):
    def mapServiceToDto(self, service: Job) -> ServiceDto:
        return ServiceDto(id=service.id, description=service.description, cost_value=service.cost_value)

    def mapDtoToService(self, dto: ServiceDto) -> Job:
        return Job(desciption=dto.description, cost_value=dto.cost_value)