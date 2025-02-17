from models.comment import Comment
from models.user import User
from models.project import Project
from models.task import Task
from sqlmodel import Session
from datetime import datetime

def create_fixtures(session: Session):
    user1 = User(email="user1@example.com")
    user2 = User(email="user2@example.com")
    session.add(user1)
    session.add(user2)
    session.commit()

    project1 = Project(
        slug="project1", 
        name="Project 1", 
        description="Description of Project 1", 
        createdAt=datetime.now().isoformat(), 
        updatedAt=datetime.now().isoformat()
    )
    project2 = Project(
        slug="project2", 
        name="Project 2", 
        description="Description of Project 2", 
        createdAt=datetime.now().isoformat(), 
        updatedAt=datetime.now().isoformat()
    )
    session.add(project1)
    session.add(project2)
    session.commit()

    task1 = Task(
        title="Task 1", 
        description="Description for Task 1", 
        status="pending", 
        project_id=project1.id
    )
    task2 = Task(
        title="Task 2", 
        description="Description for Task 2", 
        status="in-progress", 
        project_id=project1.id
    )
    task3 = Task(
        title="Task 3", 
        description="Description for Task 3", 
        status="completed", 
        project_id=project2.id
    )
    session.add(task1)
    session.add(task2)
    session.add(task3)
    session.commit()

    comment1 = Comment(
        content="Great project!", 
        author_id=user1.id, 
        project_id=project1.id
    )
    comment2 = Comment(
        content="I love working on this!", 
        author_id=user2.id, 
        project_id=project1.id
    )
    session.add(comment1)
    session.add(comment2)
    session.commit()
