from sqlmodel import Session, select
from models.project import Project

def get_projects(session: Session):
    return session.exec(select(Project)).all()

def get_project(session: Session, project_id: int):
    return session.get(Project, project_id)

def create_project(session: Session, slug: str, name: str, description: str, createdAt: str, updatedAt: str):
    project = Project(slug=slug, name=name, description=description, createdAt=createdAt, updatedAt=updatedAt)
    session.add(project)
    session.commit()
    session.refresh(project)
    return project
