from sqlmodel import Session
from models.user import User
from models.project import Project
from models.comment import Comment
from models.task import Task
import datetime

def create_fixtures(session: Session):
    # Création d'utilisateurs
    user1 = User(email="user1@example.com")
    user2 = User(email="user2@example.com")
    session.add(user1)
    session.add(user2)
    session.commit()

    # Création de projets
    project1 = Project(slug="project1", name="Project 1", description="Description for project 1",
                       createdAt=str(datetime.datetime.now()), updatedAt=str(datetime.datetime.now()))
    project2 = Project(slug="project2", name="Project 2", description="Description for project 2",
                       createdAt=str(datetime.datetime.now()), updatedAt=str(datetime.datetime.now()))
    session.add(project1)
    session.add(project2)
    session.commit()

    # Création de tâches
    task1 = Task(title="Task 1", description="Description for task 1", status="In Progress", author_id=user1.id, project_id=project1.id)
    task2 = Task(title="Task 2", description="Description for task 2", status="Completed", author_id=user2.id, project_id=project2.id)
    session.add(task1)
    session.add(task2)
    session.commit()

    # Création de commentaires
    comment1 = Comment(content="Great project!", author_id=user1.id, project_id=project1.id)
    comment2 = Comment(content="Looking forward to it!", author_id=user2.id, project_id=project2.id)
    session.add(comment1)
    session.add(comment2)
    session.commit()
