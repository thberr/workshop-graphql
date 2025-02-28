from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from models.project import Project
from models.user import User


class Comment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(index=True)
    author_id: Optional[int] = Field(default=None, foreign_key="user.id")
    project_id: Optional[int] = Field(default=None, foreign_key="project.id")

    project: Optional["Project"] = Relationship(back_populates="comments")
    author: Optional["User"] = Relationship(back_populates="comments")
