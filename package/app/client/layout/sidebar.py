from dataclasses import dataclass
from typing import Dict, List, Set, Type
from package.app.api.enum.RoleEnum import RoleEnum
from package.app.client.modules.login.LoginView import LoginView
from package.app.template.IAppComponent import IAppComponent


@dataclass
class SidebarItem:
    component: Type[IAppComponent]
    roles: Set[RoleEnum]


sidebarItems: Dict[str, SidebarItem] = {
    "component1": SidebarItem(
        component=LoginView,
        roles={RoleEnum.GERENTE, RoleEnum.FUNCIONARIO},
    ),
    "component2": SidebarItem(
        component=LoginView,
        roles={RoleEnum.GERENTE, RoleEnum.FUNCIONARIO},
    ),
    "component3": SidebarItem(
        component=LoginView,
        roles={RoleEnum.GERENTE, RoleEnum.FUNCIONARIO},
    ),
    "component4": SidebarItem(
        component=LoginView,
        roles={RoleEnum.GERENTE, RoleEnum.FUNCIONARIO},
    ),
    "component5": SidebarItem(
        component=LoginView,
        roles={RoleEnum.GERENTE, RoleEnum.FUNCIONARIO},
    ),
}
