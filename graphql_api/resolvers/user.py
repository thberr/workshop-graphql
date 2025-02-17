from sqlmodel import Session
import strawberry
from typing import List
from crud.user import create_user, get_users, get_user
from strawberry.types import Info
from graphql_api.types import User

@strawberry.type
class UserQuery:
    @strawberry.field
    def users(self, info: Info) -> List[User]:
        session = info.context.get("session")
        if session is None:
            raise ValueError("Session is missing from context")
        return get_users(session)

    @strawberry.field
    def user(self, user_id: int, info: Info) -> User:
        session = info.context.get("session")
        if session is None:
            raise ValueError("Session is missing from context")
        return get_user(session, user_id)

@strawberry.type
class UserMutation:
    @strawberry.mutation
    def add_user(self, email: str, info: strawberry.Info) -> User:
        session: Session = info.context["session"]
        return create_user(session, email)