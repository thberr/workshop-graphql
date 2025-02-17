from sqlmodel import Session, select
from models.comment import Comment

def get_comments(session: Session):
    return session.exec(select(Comment)).all()

def get_comment(session: Session, comment_id: int):
    return session.get(Comment, comment_id)

def create_comment(session: Session, content: str, author_id: int, project_id: int):
    comment = Comment(content=content, author_id=author_id, project_id=project_id)
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment
