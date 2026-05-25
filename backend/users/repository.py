from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from schemas import UserCreate, UserUpdate


async def get_users(
    session: AsyncSession
) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return users


async def get_user_by_id(
    session: AsyncSession,
    user_id: int
) -> Optional[User]:
    return await session.get(User, user_id)


async def get_user_by_username(
    session: AsyncSession,
    username: str
) -> Optianal[User]:
    stmt = select(User).where(
        User.username == username
    )
    user = await session.execute(stmt)
    return user


async def create_user(
    session: AsyncSession,
    user_in: UserCreate
) -> User: 
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    return user


async def update_user(
    session: AsyncSession,
    user: User,
    user_update: UserUpdate
) -> User:
    for name, value in user_update.model_dump().items():
        setattr(user, name, value)
    await session.commit()


async def delete_user(
    session: AsyncSession,
    user_in: User
) -> None:
    await session.delete(user_in)
    await session.commit()
