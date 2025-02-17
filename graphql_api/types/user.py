import strawberry
from typing import List
from strawberry import LazyType

@strawberry.type
class User:
    id: int
    email: str
    comments: List[LazyType("Comment", module="graphql_api.types.comment")]  # Correct
