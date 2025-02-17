from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from models.user import User
from models.project import Project

class Comment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(index=True)
    author_id: Optional[int] = Field(default=None, foreign_key="user.id")
    project_id: Optional[int] = Field(default=None, foreign_key="project.id")

    project: Optional["Project"] = Relationship(back_populates="comments")
    author: Optional["User"] = Relationship(back_populates="comments")
