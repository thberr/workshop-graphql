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

def get_context(session: Session = Depends(get_session)):
    return {"session": session}

graphql_app = GraphQLRouter(schema, context_getter=get_context)

app.include_router(graphql_app, prefix="/graphql")
