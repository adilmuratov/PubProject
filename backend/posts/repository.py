from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from posts.post import Post
    from users.user import User

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.db.db_helper import db_helper
from posts.schemas import PostCreate, PostUpdate


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


async def create_post(
    session: AsyncSession,
    user: User,
    post_create: PostCreate
) -> Post:
    post = Post(
        body=post_create.body,
        user=user
    )
    session.add(post)
    await session.commit()
    

async def update_post(
    session: AsyncSession,
    post: Post,
    post_update: PostUpdate
) -> Post:
    for name, value in post_update.model_dump(exclude_unset=partial).items():
        setattr(post, name, value)
    await session.commit()
    return post


async def delete_post(
    session: AsyncSession,
    post: Post
) -> None:
    await session.delete(post)
    await session.commit()
