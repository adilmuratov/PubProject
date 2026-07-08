from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from users.user import User

from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from userstyles.userstyle import Userstyle
from userstyles.schemas import UserstyleUpdate


async def get_userstyle_by_id(
    session: AsyncSession,
    userstyle_id: int
) -> Optional[Userstyle]:
    return await session.get(Userstyle, userstyle_id)


async def create_userstyle(
    session: AsyncSession,
    user: User
): 
    userstyle = Userstyle(
        font="font",
        background_color="color",
        user=user
    )
    session.add(userstyle)
    await session.commit()


async def update_userstyle(
    session: AsyncSession,
    userstyle: Userstyle,
    userstyle_update: UserstyleUpdate
) -> Userstyle:
    for name, value in userstyle_update.model_dump(exclude_unset=partial).items():
        setattr(userstyle, name, value)
    await session.commit()
    return userstyle


async def delete_userstyle(
    session: AsyncSession,
    userstyle: Userstyle
):
    await session.delete(userstyle)
    await session.commit()