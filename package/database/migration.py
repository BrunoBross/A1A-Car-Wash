from typing import Any, List
from package.app.api.crypt.utils import encrypt
from package.app.api.model.ResignationType import ResignationType
from package.app.api.model.Role import Role
from package.app.api.model.SchedulingState import SchedulingState

from package.app.api.model.User import User


def createMigration() -> List[Any]:
    return [
        Role(id=1, description="GERENTE"),
        Role(id=2, description="FUNCIONARIO"),
        User(username="admin", password=encrypt("senha"), role_id=1),
        SchedulingState(id=1, description="PENDENTE"),
        SchedulingState(id=2, description="FINALIZADO"),
        SchedulingState(id=3, description="JUSTIFICATIVA_1"),
        SchedulingState(id=4, description="JUSTIFICATIVA_2"),
        SchedulingState(id=5, description="JUSTIFICATIVA_3"),
        SchedulingState(id=6, description="JUSTIFICATIVA_4"),
        ResignationType(id=1, description="JUSTA_CAUSA"),
        ResignationType(id=2, description="SEM_JUSTA_CAUSA"),
    ]
