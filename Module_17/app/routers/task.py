from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
# Функция создания slug-строки
from slugify import slugify
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session

# Функция подключения к БД
from app.backend.db_depends import get_db
from app.models import Task, User
from app.schemas import CreateTask, UpdateTask


router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def get_all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get("/task_id")
async def get_task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found!'
        )
    return task


@router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], user_id: int, create_task: CreateTask):
    user = db.scalar(select(User).where(User.id == user_id))

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='User was not found!'
        )

    db.execute(insert(Task).values(
        title=create_task.title,
        content=create_task.content,
        priority=create_task.priority,
        user_id=user_id
    ))

    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful!'
    }


@router.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)], user_id: int, update_task: UpdateTask):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found!'
        )
    db.execute(update(User).where(User.id == user_id).values(
        title=update_task.title,
        content=update_task.content,
        priority=update_task.priority))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task update is successful!'
    }


@router.delete("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)], user_id: int, task_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found!'
        )
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found!'
        )
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task was deleted!'
    }
