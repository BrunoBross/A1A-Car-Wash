from __future__ import annotations
from typing import Protocol


class IAppModule(Protocol):
    def start(self) -> None:
        ...
