from typing import List

import strawberry
from sqlmodel import Session
from strawberry.types import Info

from crud.project import create_project, get_project, get_projects
from graphql_api.types import ProjectType


@strawberry.type
class ProjectQuery:
    @strawberry.field
    def projects(self, info: Info) -> List[ProjectType]:
        session = info.context.get("session")
        if session is None:
            raise ValueError("Session is missing from context")
        return get_projects(session)

    @strawberry.field
    def project(self, project_id: int, info: Info) -> ProjectType:
        session = info.context.get("session")
        if session is None:
            raise ValueError("Session is missing from context")
        return get_project(session, project_id)

@strawberry.type
class ProjectMutation:
    @strawberry.mutation
    def add_project(
        self, slug: str, name: str, description: str, createdAt: str, updatedAt: str, info: strawberry.Info
    ) -> ProjectType:
        session: Session = info.context["session"]
        return create_project(session, slug, name, description, createdAt, updatedAt)
    
    @strawberry.mutation
    def updateProject(self, projectId: int, slug: str, name: str, description: str, createdAt: str, updatedAt: str, session: strawberry.Info) -> ProjectType:
        session = session.context.get("session")
        project = get_project(session, projectId)
        if project:
            project.slug = slug
            project.name = name
            project.description = description
            project.createdAt = createdAt
            project.updatedAt = updatedAt
            session.add(project)
            session.commit()
            session.refresh(project)
            return project
        raise Exception("Project not found")
    
    @strawberry.mutation
    def deleteProject(self, projectId: int, session: strawberry.Info) -> ProjectType:
        session = session.context.get("session")
        project = get_project(session, projectId)
        if project:
            session.delete(project)
            session.commit()
            return project
        raise Exception("Project not found")