from typing import Optional

from sqlmodel import SQLModel


class UserRead(SQLModel):
    id: int
    first_name: Optional[str]
    last_name: Optional[str]
    email: str


class UserCreate(SQLModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: str
    password: str


class UserUpdate(SQLModel):
    first_name: Optional[str]
    last_name: Optional[str]
