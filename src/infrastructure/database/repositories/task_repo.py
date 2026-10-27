from sqlalchemy.orm import Session
from application.interfaces.task_repository import TaskRepositoryProtocol
from domain.entities.task import Task, Priority
from infrastructure.database.models.task_model import TaskModel
from infrastructure.database.models.mappers import TaskMapper

class SqlAlchemyTaskRepository(TaskRepositoryProtocol):
    def __init__(self, session: Session):
        self.session = session

    def save(self, task: Task) -> None:
        task_model = TaskMapper.to_orm(task)
        self.session.merge(task_model)

    def get_by_id(self, task_id: str) -> Task | None:
        model = self.session.get(TaskModel, task_id)
        if model is None:
            return None
        return TaskMapper.from_orm(model)

    def get_by_priority(self, priority: Priority) -> list[Task]:
        models = self.session.query(TaskModel).filter_by(priority=priority.value).all()
        return [TaskMapper.from_orm(model) for model in models]
