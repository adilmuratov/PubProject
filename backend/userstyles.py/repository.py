from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from models import Userstyle
from schemas import UserstyleUpdate


async def get_userstyle_by_id(
    session: AsyncSession,
    userstyle_id: int
) -> Optional[Userstyle]:
    return await session.get(Userstyle, userstyle_id)


async def update_userstyle(
    session: AsyncSession,
    userstyle: Userstyle,
    userstyle_update: UserstyleUpdate
) -> Userstyle:
    for name, value in userstyle_update.model_dump().items():
        setattr(userstyle, name, value)
    await session.commit()
    return userstyle