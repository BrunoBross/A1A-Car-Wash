from dataclasses import dataclass
from typing import Dict, Set, Type
from package.app.api.enum.RoleEnum import RoleEnum
from package.app.client.modules.employee.EmployeeView import EmployeeView
from package.app.client.modules.registeremployee.RegisterEmployeeView import (
    RegisterEmployeeView,
)
from package.app.client.modules.registervehicle.RegisterVehicleView import (
    RegisterVehicleView,
)
from package.app.template.IAppComponent import IAppComponent


@dataclass
class SidebarItem:
    component: Type[IAppComponent]
    roles: Set[RoleEnum]


sidebarItems: Dict[str, SidebarItem] = {
    "Cadastrar Funcionário": SidebarItem(
        component=RegisterEmployeeView,
        roles={RoleEnum.GERENTE},
    ),
    "Tela Teste Funcionário": SidebarItem(
        component=EmployeeView,
        roles={RoleEnum.FUNCIONARIO},
    ),
    "Cadastrar Veiculos": SidebarItem(
        component=RegisterVehicleView,
        roles={RoleEnum.GERENTE},
    ),
}
