from types import TracebackType
from sqlalchemy.orm import sessionmaker, Session
from application.interfaces.uow import UnitOfWorkProtocol
from infrastructure.database.repositories.task_repo import SqlAlchemyTaskRepository

class SqlAlchemyUnitOfWork(UnitOfWorkProtocol):
    def __init__(self, session_factory: sessionmaker[Session]):
        self.session_factory = session_factory

    def __enter__(self) -> "SqlAlchemyUnitOfWork":
        self.session = self.session_factory()
        self.tasks = SqlAlchemyTaskRepository(self.session)
        return self

    def __exit__(
        self, 
        exc_type: type[BaseException] | None, 
        exc: BaseException | None, 
        tb: TracebackType | None
    ) -> None:
        if exc_type is not None:
            self.rollback()
        self.session.close()

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()
