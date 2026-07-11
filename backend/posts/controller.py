from typing import Annotated

from fastapi import (
    APIRouter,
    Depends, 
    status,
    Path
)

from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.db.db_helper import db_helper
from auth.dependencies.get_current_user import get_current_user
from users.user import User
from posts.schemas import PostRead, PostUpdate

from posts import service


router = APIRouter()


@router.get("/", response_model=list[PostRead])
async def get_posts(
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    return await service.get_posts(
        session=session
    )


@router.get("/{post_id}/", response_model=PostRead)
async def get_post_by_id(
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    return await service.get_post_by_id(
        post_id=post_id,
        session=session
    )


@router.post("/create/", response_model=PostRead, status_code=status.HTTP_201_CREATED)
async def create_post(
    post_create: PostCreate,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    return await service.create_post(
        post_create=post_create,
        user=user,
        session=session
    )


@router.patch("/{post_id}/edit/", response_model=PostRead)
async def update_post(
    post_id: Annotated[int, Path(gt=0)],
    post_update: PostUpdate,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    return await service.update_post(
        post_update=post_update,
        post_id=post_id,
        user=user,
        session=session
    )


@router.delete("/{post_id}/delete/", status_code=status.HTTP_202_ACCEPTED)
async def delete_post(
    post_id: Annotated[int, Path(gt=0)],
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    await service.delete_post(
        post_id=post_id,
        user=user,
        session=session
    )
