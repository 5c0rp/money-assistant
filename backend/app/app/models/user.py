from typing import Optional

from sqlmodel import Field

from .base_model import BaseModel


class User(BaseModel, table=True):
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    email: str = Field(index=True)
    hashed_password: str
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
