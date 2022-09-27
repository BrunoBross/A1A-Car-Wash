from __future__ import annotations
from abc import abstractmethod
from typing import Optional, Type


class IAppComponent:

    @abstractmethod
    def start() -> Optional[Type[IAppComponent]]: pass

