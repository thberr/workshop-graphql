from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship

class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    slug: str = Field(index=True)
    name: str = Field(index=True)
    description: str = Field(index=True)
    createdAt: str = Field(index=True)
    updatedAt: str = Field(index=True)

    comments: List["Comment"] = Relationship(back_populates="project")
    tasks: List["Task"] = Relationship(back_populates="project")
