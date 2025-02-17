from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from models.user import User
from models.project import Project

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    status: str

    author_id: Optional[int] = Field(default=None, foreign_key="user.id")
    author: Optional["User"] = Relationship(back_populates="tasks")

    project_id: Optional[int] = Field(default=None, foreign_key="project.id")
    project: Optional["Project"] = Relationship(back_populates="tasks")
