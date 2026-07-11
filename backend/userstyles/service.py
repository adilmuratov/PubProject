from sqlalchemy.ext.asyncio import AsyncSession

from userstyles import repository
from userstyles.userstyle import Userstyle
from userstyles.schemas import UserstyleUpdate
from users.user import User


async def get_userstyle_by_id(
    session: AsyncSession,
    userstyle_id: int
) -> Userstyle:
    return await repository.get_userstyle_by_id(
        session=session,
        userstyle_id=userstyle_id
    )


async def update_userstyle(
    session: AsyncSession,
    user: User,
    userstyle_update: Userstyle
) -> Userstyle:
    userstyle = user.userstyle

    return await repository.update_userstyle(
        session=session,
        userstyle=userstyle,
        userstyle_update=userstyle_update
    )