from typing import Optional

from sqlmodel import SQLModel, Field


class BaseSQLModel(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
