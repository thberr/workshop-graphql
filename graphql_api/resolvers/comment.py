from sqlmodel import Session
import strawberry
from typing import List
from crud.comment import create_comment, get_comments, get_comment
from strawberry.types import Info
from graphql_api.types import Comment

@strawberry.type
class CommentQuery:
    @strawberry.field
    def comments(self, info: Info) -> List[Comment]:
        session = info.context.get("session")
        if session is None:
            raise ValueError("Session is missing from context")
        return get_comments(session)

    @strawberry.field
    def comment(self, comment_id: int, info: Info) -> Comment:
        session = info.context.get("session")
        if session is None:
            raise ValueError("Session is missing from context")
        return get_comment(session, comment_id)

@strawberry.type
class CommentMutation:
    @strawberry.mutation
    def add_comment(
        self, content: str, author_id: int, project_id: int, info: strawberry.Info
    ) -> Comment:
        session: Session = info.context["session"]
        return create_comment(session, content, author_id, project_id)