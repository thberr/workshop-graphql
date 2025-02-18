import strawberry
from graphql_api.types.user import UserType

@strawberry.type
class LoginType:
    user: UserType
    token: str
