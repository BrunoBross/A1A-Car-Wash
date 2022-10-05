from dataclasses import dataclass
from typing import Dict, Set, Type
from package.app.api.enum.RoleEnum import RoleEnum
from package.app.client.modules.serviceRegistration.serviceRegistrationView import ServiceRegistrationView
from package.app.template.IAppComponent import IAppComponent


@dataclass
class SidebarItem:
    component: Type[IAppComponent]
    roles: Set[RoleEnum]


sidebarItems: Dict[str, SidebarItem] = {
    "Cadastrar Serviço": SidebarItem(
        component=ServiceRegistrationView,
        roles={RoleEnum.GERENTE},
    )
}
