from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship
)

from infrastructure.db.base import Base
from posts.models import Post
from userstyles.models import Userstyle
from likes.models import Like


class User(Base):
    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    username: Mapped[str] = mapped_column(
        String(24), 
        unique=True
    )

    password_hash: Mapped[bytes]

    posts: Mapped[list["Post"]] = relationship(
        back_populates="user"
    )

    comments: Mapped["Comment"] = relationship(
        back_populates="user"
    )
    
    userstyle: Mapped["Userstyle"] = relationship(
        back_populates="user", 
        uselist=False
    )

    likes: Mapped[list["Like"]] = relationship(
        back_populates="user"
    )


