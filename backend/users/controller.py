from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.db.db_helper import db_helper
from auth.dependencies.get_current_user import get_current_user
from users.user import User
from users.schemas import UserCreate, UserUpdate, UserRead

from users import service


router = APIRouter()


@router.get("/", response_model=list[UserRead])
async def get_users(
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    return await service.get_users(
        session=session
    )


@router.post("/register/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    return await service.create_user(
        user_in=user_in,
        session=session
    )


@router.get("/{user_id}/", response_model=UserRead)
async def get_user(
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    return await service.get_user(
        session=session,
        user_id=user_id
    )   


@router.patch("/", response_model=UserRead)
async def update_user(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    return await service.update_user(
        user_update=user_update,
        user=current_user,
        session=session
    )


@router.patch("/change_password/", status_code=status.HTTP_202_ACCEPTED)
async def change_password(
    old_password: str,
    new_password: str,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    await service.change_password(
        old_password=old_password,
        new_password=new_password,
        user=user,
        session=session
    )


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    await service.delete_user(
        user=current_user,
        session=session
    )
