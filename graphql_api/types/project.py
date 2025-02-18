import strawberry
from typing import List
from strawberry import LazyType

@strawberry.type
class ProjectType:
    id: int
    slug: str
    name: str
    description: str
    createdAt: str
    updatedAt: str
    comments: List[LazyType("CommentType", module="graphql_api.types.comment")]
    tasks: List[LazyType("TaskType", module="graphql_api.types.task")]
