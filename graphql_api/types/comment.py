import strawberry
from strawberry import LazyType

@strawberry.type
class CommentType:
    id: int
    content: str
    author: LazyType("UserType", module="graphql_api.types.user")
    project: LazyType("ProjectType", module="graphql_api.types.project")
