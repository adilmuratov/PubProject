from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    Path,
    status
)

from infrastructure.db.db_helper import db_helper
from auth.dependencies.get_current_user import get_current_user
from comments.schemas import CommentRead, CommentCreate, CommentUpdate
from users.user import User

from comments import service


router = APIRouter()


@router.get("/{comment_id}/", response_model=CommentRead)
async def get_comment_by_id(
    comment_id: Annotated[int, Path(gt=0)],
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    return await service.get_comment_by_id(
        comment_id=comment_id,
        session=session
    )


@router.post("/{parent_comment_id}/response/", response_model=CommentRead)
async def create_comment_to_comment(
    parent_comment_id: Annotated[int, Path(gt=0)],
    comment_create: CommentCreate,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    return await service.create_comment_to_comment(
        comment_create=comment_create,
        user=user,
        parent_comment_id=parrent_comment_id,
        session=session
    )


@router.patch("/{comment_id}/edit/", response_model=CommentRead)
async def update_comment(
    comment_id: Annotated[int, Path(gt=0)],
    comment_update: CommentUpdate,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    return await service.update_comment(
        comment_id=comment_id,
        comment_update=comment_update,
        user=user,
        session=session
    )


@router.delete("/{comment_id}/delete/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_comment(
    comment_id: Annotated[int, Path(gt=0)],
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    await service.delete_comment(
        comment_id=comment_id,
        user=user,
        session=session
    )