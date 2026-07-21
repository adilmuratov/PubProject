from typing import TYPE_CHECKING, Optianal

if TYPE_CHECKING:
    from profiles.profile import Profile
    from users.user import User

from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from profiles.schemas import ProfileUpdate


async def get_profile_by_id(
    session: AsyncSession,
    profile_id: int
) -> Optional[Profile]:
    return await session.get(Profile, profile_id)


async def create_profile(
    session: AsyncSession,
    user: User
):
    profile = Profile(
        description="",
        user=user
    )
    session.add(profile)
    await session.commit()


async def update_profile(
    session: AsyncSession,
    profile: Profile,
    profile_update: ProfileUpdate
) -> Profile:
    for name, value in profile_update.model_dump(exclude_unset=partial).items():
        setattr(profile, name, value)
    await session.commit()
    return profile


async def delete_profile(
    session: AsyncSession,
    profile: Profile
) -> None:
    await session.delete(profile),
    await session.commit()