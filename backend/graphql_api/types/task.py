import strawberry
from strawberry import LazyType


@strawberry.type
class TaskType:
    id: int
    title: str
    description: str
    completed: bool
    project: LazyType("ProjectType", module="graphql_api.types.project")
