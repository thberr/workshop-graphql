from sqlmodel import Session
import strawberry
from typing import List, Optional
from graphql_api.types import Task
from crud.task import create_task, get_tasks, get_task

@strawberry.type
class TaskQuery:
    @strawberry.field
    def tasks(self) -> List[Task]:
        return get_tasks()

    @strawberry.field
    def task(self, task_id: int) -> Task:
        return get_task(task_id)

@strawberry.type
class TaskMutation:
    @strawberry.mutation
    def add_task(
        self, title: str, description: str, status: str, projectId: int, authorId: int, info: strawberry.Info
    ) -> Task:
        session: Session = info.context["session"]
        return create_task(session, title, description, status, projectId, authorId)

    @strawberry.mutation
    def update_task(
        self, taskId: int, title: Optional[str], description: Optional[str], status: Optional[str], 
        projectId: Optional[int], authorId: Optional[int], info: strawberry.Info
    ) -> Task:
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
    def delete_task(self, taskId: int, info: strawberry.Info) -> Task:
        session: Session = info.context["session"]
        task = get_task(session, taskId)
        
        if task:
            session.delete(task)
            session.commit()
            return task
        raise Exception("Task not found")