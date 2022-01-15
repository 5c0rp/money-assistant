from typing import Optional, List, TYPE_CHECKING

from sqlmodel import Field, Relationship

from .base_model import BaseModel
from .project import UserProjectLink

if TYPE_CHECKING:
    from app.models import Project


class User(BaseModel, table=True):
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    email: str = Field(index=True)
    hashed_password: str
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    projects: List["Project"] = Relationship(back_populates="owner")
    project_set: List["Project"] = Relationship(
        back_populates="collaborators", link_model=UserProjectLink
    )
