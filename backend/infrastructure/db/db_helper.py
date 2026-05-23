from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession
)

from infrastructure.config import settings

class DataBaseHelper:
    def __init__(
        self,
        url: str,
        echo: bool = False
    ):
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False
        )
    
    def get_scopped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task
        )

    async def session_dependency(self) -> AsyncSession:
        session = self.get_scopped_session()
        yield session
        await session.close()

db_helper = DataBaseHelper(
    url=settings.db.url,
    echo=settings.db.echo
)
