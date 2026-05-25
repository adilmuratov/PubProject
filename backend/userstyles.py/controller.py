from fastapi import (
    Depends, 
    APIRouter
)

from infrastructure.db.db_helper import db_helper
from models import Userstyle
from dependencies import get_userstyle_by_id
import repository


router = APIRouter()


@router.get("/{userstyle_id}/", response_model=Userstyle)
async def get_userstyle_by_id(
    userstyle: Userstyle = Depends(get_userstyle_by_id)
):
    return userstyle


@router.patch("/{userstyle_id}", response_model=Userstyle)
async def update_userstyle_by_id(
    userstyle_update: UserstyleUpdate,
    userstyle: Userstyle = Depends(get_userstyle_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await repository.update_userstyle(
        userstyle_update=userstyle_update,
        userstyle=userstyle,
        session=session
    )
    