from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session, select
from strawberry.fastapi import GraphQLRouter
from database import create_db_and_tables, get_session
from graphql_api.schema import schema
from models.project import Project
from models.comment import Comment
from models.user import User

app = FastAPI()

SessionDep = Depends(get_session)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/users", response_model=List[User])
def get_users(session: Session = SessionDep):
    users = session.exec(select(User)).all()
    return users

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, session: Session = SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return user

@app.get("/projects", response_model=List[Project])
def get_projects(session: Session = SessionDep):
    projects = session.exec(select(Project)).all()
    return projects

@app.get("/projects/{project_id}", response_model=Project)
def get_project(project_id: int, session: Session = SessionDep):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Projet non trouvé")
    return project

@app.get("/comments", response_model=List[Comment])
def get_comments(session: Session = SessionDep):
    comments = session.exec(select(Comment)).all()
    return comments

@app.get("/comments/{comment_id}", response_model=Comment)
def get_comment(comment_id: int, session: Session = SessionDep):
    comment = session.get(Comment, comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Commentaire non trouvé")
    return comment