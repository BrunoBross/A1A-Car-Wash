from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class WarningDto:
    id: Optional[int] = field(default=None)
    description: Optional[str] = field(default=None)
    date: Optional[str] = field(default=datetime.today().strftime("%Y-%m-%d"))
