from package.app.api.modules.job.dto.JobDto import JobDto
from package.app.decorators import validator_function
from package.app.meta.Singleton import Singleton
from package.app.api.modules.job.JobQuery import JobQuery
from package.app.validation.ValidationObject import ValidationObject


class JobValidator(metaclass=Singleton):
    def __init__(self):
        self.__query = JobQuery()

    @validator_function
    def execute(self, jobDto: JobDto, validation: ValidationObject) -> bool:
        if self.__query.getJobByDescription(jobDto.description):
            validation.errors.add(
                f"Serviço '{jobDto.description}' já cadastrado. Por favor tente um valor diferente."
            )
            return False
        return True
