from typing import Any, List
from package.app.api.crypt.utils import encrypt
from package.app.api.model.ResignationType import ResignationType
from package.app.api.model.Role import Role
from package.app.api.model.SchedulingState import SchedulingState
from package.app.api.model.Employee import Employee
from package.app.api.model.Job import Job
from package.app.api.model.Vehicle import Vehicle
from package.app.api.model.Scheduling import Scheduling
from datetime import datetime

from package.app.api.model.User import User


def createMigration() -> List[Any]:
    return [
        Role(id=1, description="GERENTE"),
        Role(id=2, description="FUNCIONARIO"),
        User(username="admin", password=encrypt("senha"), role_id=1),
        SchedulingState(id=1, description="PENDENTE"),
        SchedulingState(id=2, description="FINALIZADO"),
        SchedulingState(id=3, description="Funcionario Ausente"),
        SchedulingState(id=4, description="Cliente Ausente"),
        SchedulingState(id=5, description="Equipamento com defeito"),
        #SchedulingState(id=6, description="JUSTIFICATIVA_4"),
        ResignationType(id=1, description="JUSTA_CAUSA"),
        ResignationType(id=2, description="SEM_JUSTA_CAUSA"),
        #Debug
        User(username="Funça", password=encrypt("senha"), role_id=2),
        Employee(user_id = 2, legal_name="Serginho", wage=1200.50),  
        Job(description="Enceramento", cost_value=500.99),
        Vehicle(numberPlate="ELL5050"),
        Scheduling(employee_id=1,job_id=1,vehicle_id=1, date=datetime.now().date(), job_state_id=1)
    ]
