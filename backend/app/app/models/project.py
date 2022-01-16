from typing import Optional, List, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

from .base_model import BaseSQLModel

if TYPE_CHECKING:
    from app.models import User
    from app.models import Category


class UserProjectLink(SQLModel, table=True):
    user_id: Optional[int] = Field(
        default=None, foreign_key="user.id", primary_key=True
    )
    project_id: Optional[int] = Field(
        default=None, foreign_key="project.id", primary_key=True
    )


class Project(BaseSQLModel, table=True):
    name: str = Field()
    owner_id: int = Field(foreign_key="user.id")
    owner: "User" = Relationship(back_populates="projects")
    categories: List["Category"] = Relationship(back_populates="project")
    collaborators: List["User"] = Relationship(
        back_populates="project_set", link_model=UserProjectLink
    )
