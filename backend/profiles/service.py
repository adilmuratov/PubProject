from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from profiles.profile import Profile
    from users.user import User

from sqlalchemy.ext.asyncio import AsyncSession

from profiles import repository

from profiles.schemas import ProfileUpdate 


async def get_profile_by_id(
    session: AsyncSession,
    profile_id: int
) -> ProfileRead:
    profile = await repository.get_profile_by_id(
        session=session,
        profile_id=profile_id
    )

    return ProfileRead(
        description=profile.description
    )


async def update_profile(
    session: AsyncSession,
    user: User,
    profile_update: ProfileUpdate
) -> ProfileRead:
    user_profile = user.profile

    profile = await repository.update_profile(
        session=session,
        profile=user_profile,
        profile_update=profile_update
    )

    return ProfileRead(
        description=profile.description
    )