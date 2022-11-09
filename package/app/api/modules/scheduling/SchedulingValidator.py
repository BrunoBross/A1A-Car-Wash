from package.app.api.modules.employee.EmployeeQuery import EmployeeQuery
from package.app.api.modules.job.JobQuery import JobQuery
from package.app.api.modules.scheduling.SchedulingQuery import SchedulingQuery
from package.app.api.modules.scheduling.dto.SchedulingDto import SchedulingDto
from package.app.api.modules.vehicle.VehicleQuery import VehicleQuery
from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.validation.ValidationObject import ValidationObject


class SchedulingValidator(metaclass=Singleton):
    def __init__(self):
        self.__employeeQuery = EmployeeQuery()
        self.__jobQuery = JobQuery()
        self.__vehicleQuery = VehicleQuery()
        self.__schedulingQuery = SchedulingQuery()

    @validator_function
    def execute(
        self, schedulingDto: SchedulingDto, validation: ValidationObject
    ) -> bool:
        return self.__validateIds(
            schedulingDto, validation
        ) and self.__validateNotRepeated(schedulingDto, validation)

    def __validateIds(
        self, schedulingDto: SchedulingDto, validation: ValidationObject
    ) -> bool:
        if not (
            self.__employeeQuery.getEmployee(schedulingDto.employee.id)
            and self.__jobQuery.getJob(schedulingDto.job.id)
            and self.__vehicleQuery.getVehicle(schedulingDto.vehicle.id)
        ):
            validation.errors.add("IDs de entidade informados inválidos!")
            return False
        return True

    def __validateNotRepeated(
        self, schedulingDto: SchedulingDto, validation: ValidationObject
    ) -> bool:
        if self.__schedulingQuery.getScheduling(
            schedulingDto.employee.id, schedulingDto.vehicle.id, schedulingDto.job.id
        ):
            validation.errors.add("Tentativa de registro repetido!")
            return False
        return True
