from abc import abstractmethod
from typing import Any, Optional


class IAppModule:
    @abstractmethod
    def start(_: Optional[Any]) -> None:
        pass
