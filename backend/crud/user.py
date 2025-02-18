from sqlmodel import Session, select

from models.user import User
from utils import hash_password


def get_users(session: Session):
    statement = select(User)
    result = session.exec(statement).all() 
    return result

def get_user(session: Session, user_id: int):
    return session.get(User, user_id)

def create_user(session: Session, email: str, password: str) -> User:
    hashed_password = hash_password(password)
    user = User(email=email, password=hashed_password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
