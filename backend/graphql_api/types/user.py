from typing import List

import strawberry
from strawberry import LazyType


@strawberry.type
class UserType:
    id: int
    email: str
    password: str

    comments: List[LazyType("CommentType", module="graphql_api.types.comment")]
    tasks: List[LazyType("TaskType", module="graphql_api.types.task")]
