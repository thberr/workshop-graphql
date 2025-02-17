import strawberry
from typing import List
from graphql_api.types import Task
from crud.task import get_tasks, get_task

@strawberry.type
class TaskQuery:
    @strawberry.field
    def tasks(self) -> List[Task]:
        return get_tasks()

    @strawberry.field
    def task(self, task_id: int) -> Task:
        return get_task(task_id)

strawberry.type
class TaskMutation:
    @strawberry.mutation
    def addTask(self, title: str, description: str, project_id: int, user_id: int) -> Task:
        return create_task(title=title, description=description, project_id=project_id, user_id=user_id)

    @strawberry.mutation
    def updateTask(self, task_id: int, title: str, description: str, completed: bool) -> Task:
        return update_task(task_id=task_id, title=title, description=description, completed=completed)

    @strawberry.mutation
    def deleteTask(self, task_id: int) -> Task:
        return delete_task(task_id=task_id)