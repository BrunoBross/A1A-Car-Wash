from package.app.api.model.Job import Job
from package.app.api.modules.job.dto.JobDto import JobDto
from package.app.meta.Singleton import Singleton


class JobDtoMapper(metaclass=Singleton):
    def mapJobToDto(self, job: Job) -> JobDto:
        return JobDto(
            id=job.id,
            description=job.description,
            cost_value=job.cost_value,
        )

    def mapDtoToJob(self, dto: JobDto) -> Job:
        return Job(description=dto.description, cost_value=dto.cost_value)
