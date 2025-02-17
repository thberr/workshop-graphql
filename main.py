from fastapi import FastAPI, Depends
from sqlmodel import Session
from strawberry.fastapi import GraphQLRouter
from database import create_db_and_tables, get_session, engine
from fixtures import create_fixtures
from graphql_api.schema import schema

app = FastAPI()

SessionDep = Depends(get_session)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

    with Session(engine) as session:
        create_fixtures(session)

def get_context(session: Session = Depends(get_session)):
    return {"session": session}

graphql_app = GraphQLRouter(schema, context_getter=get_context)

app.include_router(graphql_app, prefix="/graphql")
