from typing import List

from sqlmodel import Field, Relationship, SQLModel


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    password: str

    comments: List["Comment"] = Relationship(back_populates="author")
    tasks: List["Task"] = Relationship(back_populates="author")
