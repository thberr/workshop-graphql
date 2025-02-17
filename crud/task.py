from sqlmodel import Session, select
from models.task import Task

def get_tasks(session: Session):
    return session.exec(select(Task)).all()

def get_task(session: Session, task_id: int):
    return session.get(Task, task_id)

def create_task(session: Session, title: str, description: str, project_id: int, user_id: int):
    task = Task(title=title, description=description, project_id=project_id, user_id=user_id)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def update_task(session: Session, task_id: int, title: str, description: str, completed: bool):
    task = session.get(Task, task_id)
    if task:
        task.title = title
        task.description = description
        task.completed = completed
        session.commit()
        session.refresh(task)
    return task

def delete_task(session: Session, task_id: int):
    task = session.get(Task, task_id)
    if task:
        session.delete(task)
        session.commit()
    return task
