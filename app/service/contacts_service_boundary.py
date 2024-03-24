from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ContactInput:
    name: str
    phone: str
    email: Optional[str] = None


@dataclass(frozen=True)
class UpdateContactInput:
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None


@dataclass(frozen=True)
class ContactOutput:
    id: str
    name: str
    phone: str
    email: Optional[str] = None
