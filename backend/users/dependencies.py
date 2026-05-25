from typing import Annotated

from fastapi import Path, APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.db.db_helper import db_helper
from schemas import User
import repository


async def get_user_by_id(
    user_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency())
) -> User:
    user = await repository.get_user_by_id(
        session=session, 
        user_id=user_id
    )
    if user is not None:
        return user
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User {user_id} not found!"
    )

async def check_existing_user_by_username(
    username: str,
    session: AsyncSession
):
    user = await repository.get_user_by_username(
        session=session,
        username=username
    )

    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User {username} already exists choose other username!"
        )