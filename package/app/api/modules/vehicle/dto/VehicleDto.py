from dataclasses import dataclass, field
from typing import Optional


@dataclass
class VehicleDto:
    id: Optional[int] = field(default=None)
    numberPlate: Optional[str] = field(default=None)
