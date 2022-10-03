from dataclasses import dataclass
from typing import Dict, Set, Type
from package.app.api.enum.RoleEnum import RoleEnum
from package.app.client.modules.exemplo.ExemploView import ExemploView
from package.app.template.IAppComponent import IAppComponent


@dataclass
class SidebarItem:
    component: Type[IAppComponent]
    roles: Set[RoleEnum]


sidebarItems: Dict[str, SidebarItem] = {
    "component1": SidebarItem(
        component=ExemploView,
        roles={RoleEnum.GERENTE, RoleEnum.FUNCIONARIO},
    ),
    "component2": SidebarItem(
        component=ExemploView,
        roles={RoleEnum.GERENTE, RoleEnum.FUNCIONARIO},
    ),
    "component3": SidebarItem(
        component=ExemploView,
        roles={RoleEnum.GERENTE, RoleEnum.FUNCIONARIO},
    ),
    "component4": SidebarItem(
        component=ExemploView,
        roles={RoleEnum.GERENTE, RoleEnum.FUNCIONARIO},
    ),
    "component5": SidebarItem(
        component=ExemploView,
        roles={RoleEnum.GERENTE, RoleEnum.FUNCIONARIO},
    ),
}
