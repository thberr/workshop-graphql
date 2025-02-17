import strawberry
from typing import List
from strawberry import LazyType

@strawberry.type
class Task:
    id: int
    title: str
    description: str
    completed: bool
    project: LazyType("Project", module="graphql_api.types.project")
    user: LazyType("User", module="graphql_api.types.user")
