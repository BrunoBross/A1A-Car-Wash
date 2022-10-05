from package.app.api.modules.job.dto.JobDto import JobDto
from package.app.meta.Singleton import Singleton


class RegisterJobValidator(metaclass=Singleton):
    def execute(self, jobDto: JobDto) -> bool:
        if not (bool(jobDto.description) and bool(jobDto.cost_value)):
            print("Preencha todos os campos!")
            return False
        return True
