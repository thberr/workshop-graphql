from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)

    comments: List["Comment"] = Relationship(back_populates="author")
    tasks: List["Task"] = Relationship(back_populates="author")
