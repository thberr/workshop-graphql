from sqlmodel import Session
import strawberry
from typing import List
from crud.comment import create_comment, get_comments, get_comment
from graphql_api.types import Comment

@strawberry.type
class CommentQuery:
    @strawberry.field
    def comments(self, info: strawberry.Info) -> List[Comment]:
        session = info.context.session
        return get_comments(session)

    @strawberry.field
    def comment(self, comment_id: int, info: strawberry.Info) -> Comment:
        session = info.context.session
        return get_comment(session, comment_id)

@strawberry.type
class CommentMutation:
    @strawberry.mutation
    def add_comment(
        self, content: str, author_id: int, project_id: int, info: strawberry.Info
    ) -> Comment:
        session: Session = info.context["session"]
        return create_comment(session, content, author_id, project_id)