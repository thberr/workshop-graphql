import strawberry
from typing import List
from strawberry import LazyType

@strawberry.type
class Comment:
    id: int
    content: str
    author: LazyType("User", module="graphql_api.types.user")  # Correct
    project: LazyType("Project", module="graphql_api.types.project")  # Correct
