import strawberry
from typing import List
from strawberry import LazyType

@strawberry.type
class Project:
    id: int
    slug: str
    name: str
    description: str
    createdAt: str
    updatedAt: str
    comments: List[LazyType("Comment", module="graphql_api.types.comment")]  # Correct
