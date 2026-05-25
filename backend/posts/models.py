from sqlalchemy.orm import (
    Mapped,
    mapped_collumn,
    relationship
)

from infrastructure.db.base import Base
from users.models import User
from comments.models import Comment
from likes.models import Like


class Post(Base):
    id: Mapped[int] = mapped_collumn(
        primary_key=True
    )

    body: Mapped[str] = mapped_collumn(
        String(1000)
    )

    user_id: Mapped[int] = mapped_collumn(
        Foreignkey("user.id"),
        unique=True 
    )

    comment_id: Mapped[int] = mapped_collumn(
        ForeignKey("user.id"),
        unique=True 
    )

    like_id: Mapped[int] = mapped_collumn(
        ForeignKey("user.id"),
        unique=True 
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