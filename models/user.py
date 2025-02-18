from sqlmodel import Relationship, SQLModel, Field
from typing import List

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    password: str

    comments: List["Comment"] = Relationship(back_populates="author")
    tasks: List["Task"] = Relationship(back_populates="author")
