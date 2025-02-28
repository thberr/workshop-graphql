import datetime

from sqlmodel import Session

from crud.user import hash_password
from models import Comment, Project, Task, User


def clear_existing_data(session: Session):
    session.query(Task).delete()
    session.query(Comment).delete()
    session.query(Project).delete()
    session.query(User).delete()
    session.commit()

def create_fixtures(session: Session):
    clear_existing_data(session)
    user1 = User(email="user1@example.com", password=hash_password("password1"))
    user2 = User(email="user2@example.com", password=hash_password("password2"))
    session.add(user1)
    session.add(user2)
    session.commit()
    
    project1 = Project(slug="project1", name="Project 1", description="Description for project 1",
                       createdAt=datetime.datetime.now(), updatedAt=datetime.datetime.now())
    project2 = Project(slug="project2", name="Project 2", description="Description for project 2",
                       createdAt=datetime.datetime.now(), updatedAt=datetime.datetime.now())
    session.add(project1)
    session.add(project2)
    session.commit()

    task1 = Task(title="Task 1", description="Description for task 1", status="In Progress", author_id=user1.id, project_id=project1.id)
    task2 = Task(title="Task 2", description="Description for task 2", status="Completed", author_id=user2.id, project_id=project2.id)
    session.add(task1)
    session.add(task2)
    session.commit()

    comment1 = Comment(content="Great project!", author_id=user1.id, project_id=project1.id)
    comment2 = Comment(content="Looking forward to it!", author_id=user2.id, project_id=project2.id)
    session.add(comment1)
    session.add(comment2)
    session.commit()
