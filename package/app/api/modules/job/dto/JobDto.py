from dataclasses import dataclass, field
from typing import Optional


@dataclass
class JobDto:
    id: Optional[int] = field(default=None)
    description: Optional[str] = field(default=None)
    cost_value: Optional[float] = field(default=None)
