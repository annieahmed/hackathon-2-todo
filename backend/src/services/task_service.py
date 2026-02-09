from sqlmodel import Session, select
from typing import List, Optional
from uuid import UUID
from ..models.task import Task, TaskCreate, TaskUpdate
from ..models.user import User
from ..utils.responses import error_response


def create_task(*, session: Session, task_in: TaskCreate, user_id: UUID) -> Task:
    """
    Create a new task for a user
    """
    # Create the task object with the user_id
    task = Task.model_validate(task_in)
    task.user_id = user_id
    
    # Add to session and commit
    session.add(task)
    session.commit()
    session.refresh(task)
    
    return task


def get_tasks_by_user(*, session: Session, user_id: UUID) -> List[Task]:
    """
    Get all tasks for a specific user
    """
    statement = select(Task).where(Task.user_id == user_id)
    tasks = session.exec(statement).all()
    return tasks


def get_task_by_id_and_user(*, session: Session, task_id: UUID, user_id: UUID) -> Optional[Task]:
    """
    Get a specific task by ID and user ID
    """
    statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
    task = session.exec(statement).first()
    return task


def update_task(*, session: Session, task: Task, task_update: TaskUpdate) -> Task:
    """
    Update a task
    """
    # Update only the fields that are provided in task_update
    for field, value in task_update.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    
    session.add(task)
    session.commit()
    session.refresh(task)
    
    return task


def delete_task(*, session: Session, task: Task) -> None:
    """
    Delete a task
    """
    session.delete(task)
    session.commit()


def toggle_task_completion(*, session: Session, task: Task) -> Task:
    """
    Toggle the completion status of a task
    """
    task.completed = not task.completed
    session.add(task)
    session.commit()
    session.refresh(task)
    
    return task