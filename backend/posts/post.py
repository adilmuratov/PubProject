from typing import TYPE_CHECKING

from datetime import datetime, UTC

if TYPE_CHECKING:
    from users.user import User
    from comments.comment import Comment
    from likes.like import Like

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from sqlalchemy import String, ForeignKey, DateTime

from infrastructure.db.base import Base


class Post(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    body: Mapped[str] = mapped_column(
        String(1000)
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC)
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    user: Mapped["User"] = relationship(
        back_populates="posts"
    )

    comments: Mapped[list["Comment"]] = relationship(
        back_populates="posts",
        cascade="all, delete-orphan"
    )

    likes: Mapped[list["Like"]] = relationship(
        back_populates="posts"
    )