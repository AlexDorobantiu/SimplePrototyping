from dataclasses import dataclass
from typing import Optional


@dataclass
class Contact:
    id: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
