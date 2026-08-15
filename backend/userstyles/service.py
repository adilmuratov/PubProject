from sqlalchemy.ext.asyncio import AsyncSession

from userstyles import repository
from userstyles.userstyle import Userstyle
from userstyles.schemas import UserstyleRead, UserstyleUpdate
from users.user import User


async def get_userstyle_by_id(
    session: AsyncSession,
    userstyle_id: int
) -> UserstyleRead:
    userstyle = await repository.get_userstyle_by_id(
        session=session,
        userstyle_id=userstyle_id
    )
    
    return UserstyleRead(
        font=userstyle.font,
        background_color=userstyle.background_color
    )


async def update_userstyle(
    session: AsyncSession,
    user: User,
    userstyle_update: UserstyleUpdate
) -> UserstyleRead:
    user_userstyle = user.userstyle

    userstyle = await repository.update_userstyle(
        session=session,
        userstyle=user_userstyle,
        userstyle_update=userstyle_update
    )

    return UserstyleRead(
        font=userstyle.font,
        background_color=userstyle.background_color
    )