from datetime import datetime
from typing import Optional, TYPE_CHECKING

from sqlmodel import Field, Relationship, Column, DateTime, func

from .base_model import BaseSQLModel

if TYPE_CHECKING:
    from app.models import User
    from app.models import Project


class Category(BaseSQLModel, table=True):
    project_id: int = Field(foreign_key="project.id")
    project: "Project" = Relationship(back_populates="categories")
    name: str = Field()


class Payment(BaseSQLModel, table=True):
    category_id: int = Field(foreign_key="category.id")
    user_id: int = Field(foreign_key="user.id")
    user: "User" = Relationship(back_populates="payments")
    comment: Optional[str] = Field(default=None)
    price: int = Field()
    created_at: datetime = Field(
        sa_column=Column(DateTime, default=func.now())
    )
    edited: bool = Field(default=False)
    edited_at: datetime = Field(
        sa_column=Column(DateTime, default=None, onupdate=func.now())
    )


class Comment(BaseSQLModel, table=True):
    user_id: int = Field(foreign_key="user.id")
    payment_id: int = Field(foreign_key="payment.id")
    created_at: datetime = Field(
        sa_column=Column(DateTime, default=func.now())
    )
    edited: bool = Field(default=False)
    edited_at: datetime = Field(
        sa_column=Column(DateTime, default=None, onupdate=func.now())
    )
    text: str = Field()
