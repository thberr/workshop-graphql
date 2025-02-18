from sqlmodel import Session
import strawberry
from typing import List
from crud.comment import create_comment, get_comments, get_comment
from strawberry.types import Info
from graphql_api.types import CommentType

@strawberry.type
class CommentQuery:
    @strawberry.field
    def comments(self, info: Info) -> List[CommentType]:
        session = info.context.get("session")
        if session is None:
            raise ValueError("Session is missing from context")
        return get_comments(session)

    @strawberry.field
    def comment(self, comment_id: int, info: Info) -> CommentType:
        session = info.context.get("session")
        if session is None:
            raise ValueError("Session is missing from context")
        return get_comment(session, comment_id)

@strawberry.type
class CommentMutation:
    @strawberry.mutation
    def add_comment(
        self, content: str, author_id: int, project_id: int, info: strawberry.Info
    ) -> CommentType:
        session: Session = info.context["session"]
        return create_comment(session, content, author_id, project_id)
    
    @strawberry.mutation
    def updateComment(self, commentId: int, content: str, authorId: int, projectId: int, session: strawberry.Info) -> CommentType:
        session = session.context.get("session")
        comment = get_comment(session, commentId)
        if comment:
            comment.content = content
            comment.author_id = authorId
            comment.project_id = projectId
            session.add(comment)
            session.commit()
            session.refresh(comment)
            return comment
        raise Exception("Comment not found")
    
    @strawberry.mutation
    def deleteComment(self, commentId: int, session: strawberry.Info) -> CommentType:
        session = session.context.get("session")
        comment = get_comment(session, commentId)
        if comment:
            session.delete(comment)
            session.commit()
            return comment
        raise Exception("Comment not found")