from dataclasses import dataclass, field
from typing import Set


@dataclass
class ValidationObject:
    errors: Set[str] = field(default_factory=set)

    @property
    def isValid(self) -> bool:
        return not bool(self.errors)
