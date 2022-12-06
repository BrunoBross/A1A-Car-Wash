from dataclasses import dataclass
from typing import Dict, Set, Type
from package.app.api.enum.RoleEnum import RoleEnum
from package.app.client.modules.resignation.ResignationView import ResignationView
from package.app.client.modules.registerjob.RegisterJobView import RegisterJobView
from package.app.client.modules.billing.BillingView import BillingView
from package.app.client.modules.registerscheduling.RegisterSchedulingView import (
    RegisterSchedulingView,
)
from package.app.client.modules.registervehicle.RegisterVehicleView import (
    RegisterVehicleView,
)
from package.app.client.modules.registeremployee.RegisterEmployeeView import (
    RegisterEmployeeView,
)
from package.app.template.IAppComponent import IAppComponent
from package.app.client.modules.schedulingemployee.EmployeeSchedulingView import (
    EmployeeSchedulingView,
)
from package.app.client.modules.employeeReport.employeeReportView import EmployeeReportView


@dataclass
class SidebarItem:
    component: Type[IAppComponent]
    roles: Set[RoleEnum]


sidebarItems: Dict[str, SidebarItem] = {
    "Serviços": SidebarItem(
        component=RegisterJobView,
        roles={RoleEnum.GERENTE},
    ),
    "Veiculos": SidebarItem(
        component=RegisterVehicleView,
        roles={RoleEnum.GERENTE},
    ),
    "Funcionários": SidebarItem(
        component=RegisterEmployeeView,
        roles={RoleEnum.GERENTE},
    ),  
    "Agendamentos": SidebarItem(
        component=EmployeeSchedulingView,
        roles={RoleEnum.FUNCIONARIO},
    ),
    "Visualizar Faturamento": SidebarItem(
        component=BillingView,
        roles={RoleEnum.GERENTE},
    ),
    "Cadastrar Agendamento": SidebarItem(
        component=RegisterSchedulingView,
        roles={RoleEnum.GERENTE},
    ),
    "Demitir Funcionário": SidebarItem(
        component=ResignationView,
        roles={RoleEnum.GERENTE},
    ),
    "Emitir Relatorio de funcionario": SidebarItem(
        component=EmployeeReportView,
        roles={RoleEnum.GERENTE},
    ),
}
