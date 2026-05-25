from typing import Annotated

from fastapi import Path, APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.db.db_helper import db_helper
from models import Userstyle
import repository


async def get_userstyle_by_id(
    userstyle_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency)
) -> Userstyle:
    userstyle = await repository.get_userstyle_by_id(
        userstyle_id=userstyle_id,
        session=session    
    )
    
    if userstyle is not None:
        return userstyle
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Userstyle {userstyle} not found!"
    )