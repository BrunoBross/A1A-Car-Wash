from typing import Any, List
from package.app.api.crypt.utils import encrypt
from package.app.api.model.ResignationType import ResignationType
from package.app.api.model.Role import Role
from package.app.api.model.SchedulingState import SchedulingState
from package.app.api.model.Employee import Employee
from package.app.api.model.Job import Job
from datetime import date
from package.app.api.model.User import User


def createMigration() -> List[Any]:
    return [
        Role(id=1, description="GERENTE"),
        Role(id=2, description="FUNCIONARIO"),
        User(username="admin", password=encrypt("senha"), role_id=1),
        User(username="funcionario", password=encrypt("senha"), role_id=2),
        Employee(user_id=2, legal_name="Bruno Barreto", wage=1500, active_register=1, job_limit=5, admission_date=date.today()),
        SchedulingState(id=1, description="PENDENTE"),
        SchedulingState(id=2, description="FINALIZADO"),
        SchedulingState(id=3, description="CLIENTE_AUSENTE"),
        SchedulingState(id=4, description="EQUIPAMENTO_COM_DEFEITO"),
        ResignationType(id=1, description="JUSTA_CAUSA"),
        ResignationType(id=2, description="SEM_JUSTA_CAUSA"),
        Job(description="LAVACAO", cost_value=50.0),
        Job(description="ENCERAMENTO", cost_value=100.0),
    ]
