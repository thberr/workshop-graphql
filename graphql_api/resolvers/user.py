import datetime
from fastapi import HTTPException
import jwt
from sqlmodel import Session, select
import strawberry
from typing import List
from crud.user import create_user, get_users, get_user
from strawberry.types import Info
from graphql_api.types.login_type import LoginType
from graphql_api.types.user import UserType
from models.user import User
from utils import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY, verify_password

@strawberry.type
class UserQuery:
    @strawberry.field
    def users(self, info: Info) -> List[UserType]:
        session = info.context.get("session")
        if session is None:
            raise ValueError("Session is missing from context")
        return get_users(session)

    @strawberry.field
    def user(self, user_id: int, info: Info) -> UserType:
        session = info.context.get("session")
        if session is None:
            raise ValueError("Session is missing from context")
        return get_user(session, user_id)

@strawberry.type
class UserMutation:
    @strawberry.mutation
    def add_user(self, email: str, password: str, info: strawberry.Info) -> UserType:
        session: Session = info.context["session"]
        return create_user(session, email, password)

    
    @strawberry.mutation
    def update_user(self, user_id: int, email: str, info: strawberry.Info) -> UserType:
        session: Session = info.context["session"]
        user = get_user(session, user_id)
        if user:
            user.email = email
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
        raise Exception("User not found")
    
    @strawberry.mutation
    def delete_user(self, user_id: int, info: strawberry.Info) -> UserType:
        session: Session = info.context["session"]
        current_user: User = info.context["request"].state.user

        if not current_user:
            raise HTTPException(status_code=401, detail="Authentification requise")

        if current_user.id != user_id:
            raise HTTPException(status_code=403, detail="Action non autorisée")

        user = get_user(session, user_id)
        
        if user:
            session.delete(user)
            session.commit()
            return user
        
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    @strawberry.mutation
    def signup(self, email: str, password: str, info: Info) -> UserType:
        session = info.context["session"]
        user = create_user(session, email, password)
        return user
    
    @strawberry.mutation
    def login(self, email: str, password: str, info: Info) -> LoginType:
        session = info.context["session"]

        user: User = session.exec(select(User).where(User.email == email)).first()

        if user and verify_password(password, user.password):
            payload = {
                "sub": str(user.id),
                "email": user.email,
                "exp": datetime.datetime.now() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            }

            token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
            return LoginType(user=user, token=token)
        

        raise Exception("Invalid credentials")