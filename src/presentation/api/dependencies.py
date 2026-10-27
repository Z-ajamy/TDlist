# src/presentation/api/dependencies.py
from sqlalchemy.orm import sessionmaker, Session
from infrastructure.database.session import create_db_engine, get_session_maker
from infrastructure.database.uow import SqlAlchemyUnitOfWork
from application.task.create_task import CreateTaskUseCase

class DependencyContainer:
    def __init__(self):
        self.engine = create_db_engine()
        self.session_factory: sessionmaker[Session] = get_session_maker(self.engine)

    def get_uow(self) -> SqlAlchemyUnitOfWork:
        return SqlAlchemyUnitOfWork(session_factory=self.session_factory)

    def get_create_task_use_case(self) -> CreateTaskUseCase:
        uow = self.get_uow()
        return CreateTaskUseCase(uow=uow)

container = DependencyContainer()
