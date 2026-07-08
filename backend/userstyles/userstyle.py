from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship    
)
from sqlalchemy import ForeignKey

from infrastructure.db.base import Base


class Userstyle(Base):
    __tablename__ = "userstyles"
    
    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    font: Mapped[str]

    background_color: Mapped[str]

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        unique=True
    )

    user: Mapped["User"] = relationship(
        back_populates="userstyle"
    )