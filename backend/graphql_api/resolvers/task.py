from typing import List, Optional

import strawberry
from sqlmodel import Session
from strawberry.types import Info

from crud.task import create_task, get_task, get_tasks
from graphql_api.types.task import TaskType


@strawberry.type
class TaskQuery:
    @strawberry.field
    def tasks(self, info: Info) -> List[TaskType]:
        session: Session = info.context.get("session")
        if session is None:
            raise ValueError("Session is missing from context")
        return get_tasks(session)

    @strawberry.field
    def task(self, task_id: int, info: Info) -> TaskType:
        session: Session = info.context.get("session")
        if session is None:
            raise ValueError("Session is missing from context")
        return get_task(session, task_id)

@strawberry.type
class TaskMutation:
    @strawberry.mutation
    def add_task(
        self, title: str, description: str, status: str, projectId: int, authorId: int, info: strawberry.Info
    ) -> TaskType:
        session: Session = info.context["session"]
        return create_task(session, title, description, status, projectId, authorId)

    @strawberry.mutation
    def update_task(
        self, taskId: int, title: Optional[str], description: Optional[str], status: Optional[str], 
        projectId: Optional[int], authorId: Optional[int], info: strawberry.Info
    ) -> TaskType:
        session: Session = info.context["session"]
        task = get_task(session, taskId)
        
        if task:
            if title:
                task.title = title
            if description:
                task.description = description
            if status:
                task.status = status
            if projectId:
                task.project_id = projectId
            if authorId:
                task.author_id = authorId
            
            session.add(task)
            session.commit()
            session.refresh(task)
            return task
        raise Exception("Task not found")

    @strawberry.mutation
    def delete_task(self, taskId: int, info: strawberry.Info) -> TaskType:
        session: Session = info.context["session"]
        task = get_task(session, taskId)
        
        if task:
            session.delete(task)
            session.commit()
            return task
        raise Exception("Task not found")