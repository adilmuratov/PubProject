from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.db.db_helper import db_helper
from models import Post


async def get_posts(
    session: AsyncSession
) -> list[Post]:
    stmt = select(Post).order_by(Post.id)
    result: Result = await session.execute(stmt)
    posts = result.scalars().all()
    return posts


async def get_post_by_id(
    session: AsyncSession,
    post_id: int
) -> Optional[Post]:
    return await session.get(Post, post_id)

'''
async def create_post(
    session: AsyncSession,
    post: 
) -> Optional[Post]:
''' 