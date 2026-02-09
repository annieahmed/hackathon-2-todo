from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from uuid import UUID
from typing import List
from ..config.database import get_session
from ..models.task import Task, TaskCreate, TaskRead, TaskUpdate
from ..services.task_service import (
    create_task, get_tasks_by_user, get_task_by_id_and_user,
    update_task, delete_task, toggle_task_completion
)
from ..middleware.jwt_middleware import get_current_user
from ..utils.responses import success_response, error_response

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])


@router.get("/", response_model=List[TaskRead])
def get_tasks(
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Get all tasks for the authenticated user
    """
    try:
        user_id = UUID(current_user["sub"])
        tasks = get_tasks_by_user(session=session, user_id=user_id)
        return success_response(
            data={"tasks": tasks},
            message="Tasks retrieved successfully"
        )
    except Exception as e:
        raise error_response(
            error_code="SERVER_001",
            message=str(e),
            status_code=500
        )


@router.post("/", response_model=TaskRead)
def create_new_task(
    task: TaskCreate,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Create a new task for the authenticated user
    """
    try:
        # Get the user ID from the token
        user_id = UUID(current_user["sub"])
        
        db_task = create_task(session=session, task_in=task, user_id=user_id)
        return success_response(
            data={"task": db_task},
            message="Task created successfully"
        )
    except Exception as e:
        raise error_response(
            error_code="SERVER_001",
            message=str(e),
            status_code=500
        )


@router.get("/{task_id}", response_model=TaskRead)
def get_task(
    task_id: UUID,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Get a specific task by ID
    """
    try:
        user_id = UUID(current_user["sub"])
        task = get_task_by_id_and_user(session=session, task_id=task_id, user_id=user_id)
        
        if not task:
            raise error_response(
                error_code="RESOURCE_001",
                message="Task not found or does not belong to the authenticated user",
                status_code=404
            )
        
        return success_response(
            data={"task": task},
            message="Task retrieved successfully"
        )
    except ValueError:
        # Raised when task_id is not a valid UUID
        raise error_response(
            error_code="VALIDATION_001",
            message="Invalid task ID format",
            status_code=400
        )
    except Exception as e:
        raise error_response(
            error_code="SERVER_001",
            message=str(e),
            status_code=500
        )


@router.put("/{task_id}", response_model=TaskRead)
def update_existing_task(
    task_id: UUID,
    task_update: TaskUpdate,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Update a specific task by ID
    """
    try:
        user_id = UUID(current_user["sub"])
        db_task = get_task_by_id_and_user(session=session, task_id=task_id, user_id=user_id)
        
        if not db_task:
            raise error_response(
                error_code="RESOURCE_001",
                message="Task not found or does not belong to the authenticated user",
                status_code=404
            )
        
        updated_task = update_task(session=session, task=db_task, task_update=task_update)
        return success_response(
            data={"task": updated_task},
            message="Task updated successfully"
        )
    except ValueError:
        # Raised when task_id is not a valid UUID
        raise error_response(
            error_code="VALIDATION_001",
            message="Invalid task ID format",
            status_code=400
        )
    except Exception as e:
        raise error_response(
            error_code="SERVER_001",
            message=str(e),
            status_code=500
        )


@router.delete("/{task_id}")
def delete_existing_task(
    task_id: UUID,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Delete a specific task by ID
    """
    try:
        user_id = UUID(current_user["sub"])
        db_task = get_task_by_id_and_user(session=session, task_id=task_id, user_id=user_id)
        
        if not db_task:
            raise error_response(
                error_code="RESOURCE_001",
                message="Task not found or does not belong to the authenticated user",
                status_code=404
            )
        
        delete_task(session=session, task=db_task)
        return success_response(message="Task deleted successfully")
    except ValueError:
        # Raised when task_id is not a valid UUID
        raise error_response(
            error_code="VALIDATION_001",
            message="Invalid task ID format",
            status_code=400
        )
    except Exception as e:
        raise error_response(
            error_code="SERVER_001",
            message=str(e),
            status_code=500
        )


@router.patch("/{task_id}/complete", response_model=TaskRead)
def toggle_task_completion_status(
    task_id: UUID,
    current_user: dict = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Toggle the completion status of a specific task
    """
    try:
        user_id = UUID(current_user["sub"])
        db_task = get_task_by_id_and_user(session=session, task_id=task_id, user_id=user_id)
        
        if not db_task:
            raise error_response(
                error_code="RESOURCE_001",
                message="Task not found or does not belong to the authenticated user",
                status_code=404
            )
        
        toggled_task = toggle_task_completion(session=session, task=db_task)
        return success_response(
            data={"task": toggled_task},
            message="Task completion status toggled"
        )
    except ValueError:
        # Raised when task_id is not a valid UUID
        raise error_response(
            error_code="VALIDATION_001",
            message="Invalid task ID format",
            status_code=400
        )
    except Exception as e:
        raise error_response(
            error_code="SERVER_001",
            message=str(e),
            status_code=500
        )