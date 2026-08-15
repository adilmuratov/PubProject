from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from users.user import User
from users.schemas import UserCreate, UserUpdate
from auth.utils import hash_password


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
    stmt = (
        select(User)
        .where(User.username == username)
    )
    result: Result = await session.execute(stmt)
    user = result.scalars().first()
    return user


async def create_user(
    session: AsyncSession,
    user_in: UserCreate
) -> User: 
    password_hash = hash_password(user_in.password)
    user = User(
        username=user_in.username,
        password_hash=password_hash
    )
    session.add(user)
    await session.commit()
    return user


async def update_user(
    session: AsyncSession,
    user: User,
    user_update: UserUpdate
) -> User:
    for name, value in user_update.model_dump(exclude_unset=partial).items():
        setattr(user, name, value)
    await session.commit()
    return user


async def delete_user(
    session: AsyncSession,
    user: User
) -> None:
    await session.delete(user)
    await session.commit()
