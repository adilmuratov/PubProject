from datetime import datetime, UTC


from posts.post import Post
from userstyles.userstyle import Userstyle
from likes.like import Like
from profiles.profile import Profile
from comments.comment import Comment

from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship
)

from sqlalchemy import String, DateTime

from infrastructure.db.base import Base


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    username: Mapped[str] = mapped_column(
        String(24), 
        unique=True
    )

    password_hash: Mapped[bytes]

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )

    profile: Mapped["Profile"] = relationship(
        back_populates="user",
        uselist=False
    )

    userstyle: Mapped["Userstyle"] = relationship(
        back_populates="user", 
        uselist=False
    )

    posts: Mapped[list["Post"]] = relationship(
        back_populates="user"
    )

    comments: Mapped[list["Comment"]] = relationship(
        back_populates="user"
    )

    likes: Mapped[list["Like"]] = relationship(
        back_populates="user"
    )


