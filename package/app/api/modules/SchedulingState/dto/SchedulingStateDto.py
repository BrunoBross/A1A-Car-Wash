from dataclasses import dataclass, field
from typing import Optional

#from package.app.api.modules.user.dto.UserDto import UserDto


@dataclass
class SchedulingStateDto:
    id: Optional[int] = field(default=None)
    description: Optional[str] = field(default=None)
    
