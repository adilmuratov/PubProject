from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.db.db_helper import db_helper
from models import User
from dependencies import get_user_by_id, check_existing_user_by_username
from schemas import UserUpdate

import repository

router = APIRouter()


@router.get("/", response_model=list[User])
async def get_users(
    session: AsyncSession = Depends(db_helper.session_dependency())
):
    return await repository.get_users(session=session)


@router.post("/register/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    await check_existing_user_by_username(
        session=session,
        username=username
    )

    return await repository.create_user(
        session=session,
        user_in=user_in
    )


@router.get("/{user_id}/", response_model=User)
async def get_user(
    user: User = Depends(get_user_by_id)
):
    return user


@router.put("/{user_id}/", response_model=User)
async def update_user(
    user_update: UserUpdate,
    user: User = Depends(get_user_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency)
): 
    return await repository.update_user(
        session=session,
        user=user,
        user_update=user_update
    )


@router.delete("/{user_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user: User = Depends(get_user_by_id)
):
    await repository.delete_user(user_in=user)
