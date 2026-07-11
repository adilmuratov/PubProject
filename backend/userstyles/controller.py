from fastapi import (
    Depends, 
    APIRouter
)

from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.db.db_helper import db_helper
from userstyles.schemas import UserstyleRead
from users.user import User
from auth.dependencies.get_current_user import get_current_user

from userstyles import service


router = APIRouter()


@router.get("/{userstyle_id}/", response_model=UserstyleRead)
async def get_userstyle_by_id(
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    return await service.get_userstyle_by_id(
        userstyle_id=userstyle_id,
        session=session
    )


@router.patch("/", response_model=UserstyleRead)
async def update_userstyle_by_id(
    userstyle_update: UserstyleUpdate,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await service.update_userstyle(
        userstyle_update=userstyle_update,
        user=user,
        session=session
    )
    