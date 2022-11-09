from package.app.api.model.Scheduling import Scheduling
from package.app.api.modules.scheduling.dto.SchedulingDto import SchedulingDto
from package.app.meta.Singleton import Singleton


class SchedulingDtoMapper(metaclass=Singleton):
    def mapDtoToScheduling(self, dto: SchedulingDto) -> Scheduling:
        return Scheduling(
            employee_id=dto.employee.id,
            job_id=dto.job.id,
            vehicle_id=dto.vehicle.id,
            date=dto.date,
        )
