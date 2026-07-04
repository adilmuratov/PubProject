from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.db.db_helper import db_helper
from profiles.schemas import ProfileRead, ProfileUpdate
from users.user import User
from auth.dependencies.get_current_user import get_current_user

from profiles import service


router = APIRouter()


@router.get("/{profile_id}/", response_model=ProfileRead)
async def get_profile(
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    return await service.get_profile_by_id(
        profile_id=profile_id,
        session=session
    )


@router.patch("/", response_model=ProfileRead)
async def update_profile(
    profile_update: ProfileUpdate,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.get_scopped_session)
):
    return await service.update_profile(
        profile_update=profile_update,
        user=user,
        session=session
    )