from sqlmodel import Session
import strawberry
from typing import List
from crud.project import create_project, get_projects, get_project
from strawberry.types import Info
from graphql_api.types import Project

@strawberry.type
class ProjectQuery:
    @strawberry.field
    def projects(self, info: Info) -> List[Project]:
        session = info.context.get("session")
        if session is None:
            raise ValueError("Session is missing from context")
        return get_projects(session)

    @strawberry.field
    def project(self, project_id: int, info: Info) -> Project:
        session = info.context.get("session")
        if session is None:
            raise ValueError("Session is missing from context")
        return get_project(session, project_id)

@strawberry.type
class ProjectMutation:
    @strawberry.mutation
    def add_project(
        self, slug: str, name: str, description: str, createdAt: str, updatedAt: str, info: strawberry.Info
    ) -> Project:
        session: Session = info.context["session"]
        return create_project(session, slug, name, description, createdAt, updatedAt)