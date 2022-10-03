from abc import ABC, abstractmethod
from typing import Any, Optional


class Process(ABC):
    @abstractmethod
    def start(_: Optional[Any] = None) -> None:
        pass
