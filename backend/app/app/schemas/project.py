from typing import List, Optional

from sqlmodel import SQLModel

from .user import UserRead


class ProjectRead(SQLModel):
    id: int
    name: str
    owner: UserRead
    collaborators: Optional[List[UserRead]]
