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
from posts.schemas import PostRead, PostUpdate, PostCreate
from comments.schemas import CommentRead, CommentCreate

from posts import service as post_service
from comments import service as comment_service


router = APIRouter()


# @router.get("/", response_model=list[PostRead])
# async def get_posts_by_user(
#     session: AsyncSession = Depends(db_helper.get_scopped_session)
# ):
#     return await post_service.get_posts(
#         session=session
#     )


@router.get("/{post_id}/", response_model=PostRead)
async def get_post_by_id(
    post_id: Annotated[int, Path(gt=0)],
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    return await post_service.get_post_by_id(
        post_id=post_id,
        session=session
    )


@router.post("/create/", response_model=PostRead, status_code=status.HTTP_201_CREATED)
async def create_post(
    post_create: PostCreate,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    return await post_service.create_post(
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
    return await post_service.update_post(
        post_update=post_update,
        post_id=post_id,
        user=user,
        session=session
    )


@router.delete("/{post_id}/delete/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    post_id: Annotated[int, Path(gt=0)],
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    await post_service.delete_post(
        post_id=post_id,
        user=user,
        session=session
    )


@router.post("/{post_id}/like/", status_code=status.HTTP_201_CREATED)
async def create_like_to_post(
    post_id: Annotated[int, Path(gt=0)],
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    await post_service.create_like_to_post(
        post_id=post_id,
        user=user,
        session=session
    )


@router.delete("/{post_id}/like/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_like_to_post(
    post_id: Annotated[int, Path(gt=0)],
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    await post_service.delete_like_to_post(
        post_id=post_id,
        user=user,
        session=session
    )


@router.post("/{post_id}/comments/create/", response_model=CommentRead)
async def create_comment_to_post(
    post_id: Annotated[int, Path(gt=0)],
    comment_create: CommentCreate,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    return await comment_service.create_comment(
        comment_create=comment_create,
        post_id=post_id,
        user=user,
        session=session
    ) 
