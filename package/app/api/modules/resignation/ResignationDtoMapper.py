from package.app.api.model.Resignation import Resignation
from package.app.api.modules.resignation.dto.ResignationDto import ResignationDto
from package.app.meta.Singleton import Singleton


class ResignationDtoMapper(metaclass=Singleton):
    def mapResignationToDto(self, resignation: Resignation) -> ResignationDto:
        return ResignationDto(
            id=resignation.id,
            employee_id=resignation.employee_id,
            resignation_type_id=resignation.resignation_type_id,
            date=resignation.date,
            memo=resignation.memo,
            employee=resignation.employee,
            resignation_type=resignation.resignation_type,
        )

    def mapDtoToResignation(self, dto: ResignationDto) -> Resignation:
        return Resignation(
            employee_id=dto.employee_id,
            resignation_type_id=dto.resignation_type_id,
            date=dto.date,
            memo=dto.memo,
            employee=dto.employee,
            resignation_type=dto.resignation_type,
        )
