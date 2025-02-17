from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from models.project import Project
from models.user import User

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: Optional[str] = None
    completed: bool = Field(default=False)
    project_id: Optional[int] = Field(default=None, foreign_key="project.id")
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

    project: Optional[Project] = Relationship(back_populates="tasks")
    user: Optional[User] = Relationship(back_populates="tasks")
