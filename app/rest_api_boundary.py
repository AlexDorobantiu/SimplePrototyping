from typing import Optional

from pydantic import BaseModel


class ContactInput(BaseModel):
    name: str
    phone: str
    email: Optional[str] = None


class ContactOutput(BaseModel):
    id: str
    name: str
    phone: str
    email: Optional[str] = None
